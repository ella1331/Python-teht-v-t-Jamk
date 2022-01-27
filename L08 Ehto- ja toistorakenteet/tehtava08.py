#ehtolauseet
#tehtävä L08T01
#tee ohjelma jossa kysytään käyttäjältä tämän ikä.
number = int(input("Kerro ikäsi: "))
if number < 13:
    print("child")
elif number > 13 and number <= 19:
    print("teen")
elif number > 19 and number < 65:
     print("adult")
else :
    print("senior")

#funktio
#koetta varten:
#number = int(input("Kerro ikäsi: "))
def kerro3(ika):
    tulos = "unknown"
    if ika < 13:
        return("child")
    elif ika > 13 and ika <= 19:
        return("teen")
    elif ika > 20 and ika < 65:
        return("adult")
    else :
        return("senior")

#print(kerro3(5))

#L08T02
#Tee ohjelma joka kysyy käyttäjältä 3 kokonaislukua ja tulostaa niistä suurimman.
line1 = int(input("Input integer: "))
line2 = int(input("Input another integer: "))
line3 = int(input("One more: "))
if line1 > line2 and line1 > line3:
    print("Max value:",line1)
elif line2 > line3:
    print("Max value:",line2)
else:
    print("Max value:",line3)

#L08T03
'''Tee ohjelma joka kysyy käyttäjältä kokonaisluvun.
    jos luku on 10 tai 20, palauta teksti "Luku on 10 tai 20"
        jos luku on 100 tai 200, palauta teksti "Luku on 100 tai 200"
            muuten palauta annettu luku tekstinä.'''

line = int(input("Anna kokonaisluku: "))
def check_int(param1):
    if line == 10 or line == 20:
        return("Luku on 10 tai 20")
    elif line == 100 or line == 200:
        return("Luku on 100 tai 200") 
    else :
        return(line)

check_int(line)

#koetta varten

def check_int(num):
    if num == 10 or num == 20:
        return("Luku on 10 tai 20")
    elif num == 100 or num == 200:
        return("Luku on 100 tai 200") 
    else :
        return(num)

#print(check_int(10))

#L08T04
#Tee ohjelma jossa annetaan oppilaalle arvosana alla olevan taulukon mukaan.
#Kysy pistemäärä konsolissa ja tulosta arvosana.
line = int(input("Insert your points:"))
if line <= 1:
    print("Grade:0")
elif line <= 3:
    print("Grade:1")
elif line <= 5:
    print("Grade:2")
elif line <= 7:
    print("Grade:3")
elif line <= 9:
    print("Grade:4")
elif line <= 12:
    print("Grade:5")

#L08T05
'''Tee ohjelma, joka kysyy käyttäjältä viisi lukua. Laske annetuista luvuista yhteen ne luvut, jotka ovat nollaa suurempia.
Eli jos käyttäjä antaa nollan tai negatiivisen luvun sitä ei lisätä summaan. Tulosta summa konsoliin. Kokeile ohjelmaasi esim seuraavilla arvoilla: 1,2,3,4,5 ja -2,0,2,4,6. Mitä sait summaksi?'''

line = input("Input number:")
number = int (line)
if number > 0 :
    summa = number
line1 = input("Input number:")
number1 = int (line1)
if number1 > 0 :
    summa = summa + number1
line2 = input("Input number:")
number2 = int (line2)
if number2 > 0 :
    summa = summa + number2
line3 = input("Input number:")
number3 = int (line3)
if number3 > 0 :
    summa = summa + number3
line4 = input("Input number:")
number4 = int (line4)
if number4 > 0 :
    summa = summa + number4

print("Sum is",summa)

#TAI vaihtoehtoisesti sama homma for loopilla

summa = 0
for x in range(5):
    line = input("Input number:")
    number = int(line)
    if number > 0 :
        summa = summa + number

print("Sum is",summa)

#L08T06
#Tee ohjelma joka näyttää onko annettu vuosi karkausvuosi. Vuosiluku kysytään käyttäjältä.

line = int(input("Insert year:"))
if line %4 == 0 and (line %100 !=0 or line %400 == 0):
    print("Is leap year!")

else:
    print("Is not leap year!")