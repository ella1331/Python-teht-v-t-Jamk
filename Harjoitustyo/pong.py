#Yksinkertainen Pong peli
#Jatkuu niin pitkään kunnes pelaaja kyllästyy :)
#By Elina

import turtle
import winsound #tällä lisätään äänet peliin

#Määritellään ulkonäkö peliin
window = turtle.Screen()
window.title("Pong peli by Elina")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Pisteet
score_a = 0
score_b = 0

#Maila A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  #animaation nopeus
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Maila B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Pallo
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1 #pallo liikkuu 2pixeliä kerrallaan
ball.dy = -0.1

# määritellään pistetaulukkoa
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Pelaaja A: 0 Pelaaja B: 0", align="center", font=("Courier", 18, "normal"))

#Funktio mailoille ja niiden liikkumiseen
def paddle_a_up():
    y = paddle_a.ycor()     #määritellään y-koordinaatit
    y += 20                 #lisätään 20 pixeliä y-koordinaattiin
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 20            #vähennetään 20 pixeliä y-koordinaattiin
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()     #määritellään y-koordinaatit
    y += 20     #lisätään 20 pixeliä y-koordinaattiin
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 20     #vähennetään 20 pixeliä y-koordinaattiin
    paddle_b.sety(y)

#Näppäimistön määritteleminen, jolla liikutetaan mailoja
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up") #nuolinäppäimet
window.onkeypress(paddle_b_down, "Down") #nuolinäppäimet



#määritellään pelin päälooppi
while True:
    window.update()


    #Pallon liikkuminen pelissä
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Laitetaan laidat peliin

    #Ylälaita
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("way.wav", winsound.SND_ASYNC) #lisää peliin äänet

    #Alalaita
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("way.wav", winsound.SND_ASYNC)

    #Oikea laita
    if ball.xcor() > 390:
        ball.goto(0, 0) 
        ball.dx *= -1 
        score_a += 1
        pen.clear()
        pen.write("Pelaaja A: {} Pelaaja B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    #Vasen laita
    if ball.xcor() < -390:
        ball.goto(0, 0) 
        ball.dx *= -1 
        score_b += 1 
        pen.clear()
        pen.write("Pelaaja A: {} Pelaaja B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    # Mailan ja pallon kohtaaminen
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40 ):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("way.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40 ):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("way.wav", winsound.SND_ASYNC)



