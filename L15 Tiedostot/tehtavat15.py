#Tehtävä L1501
#Tee ohjelma, joka kysyy käyttäjältä henkilöiden sukunimiä ja kirjoita käyttäjän antamat nimet tiedostoon (lopetusehdon voit päättää itse).
#Avaa tämän jälkeen tiedosto lukemista varten ja tulosta konsoliin tiedoston sisältö riveittäin.
#Huomioi mahdolliset poikkeukset, joita tiedoston käsittely voi aiheuttaa.

from os import path


surnames = []
for i in range(3):
    sukunimia = str(input("Saisinko 3 sukunimeä?:"))
    sukunimia.isalpha()

    surnames.append(sukunimia)

if sukunimia.isalpha() == True:
    print("Kiitos sukunimistä :")
if sukunimia.isalpha() == False:
    print("Olisin mielummin halunnut sukunimiä")
#Avaa tämän jälkeen tiedosto lukemista varten ja tulosta konsoliin tiedoston sisältö riveittäin.
print(*surnames, sep = "\n")

#Tehtävä L1502
#Luo jollakin editorilla (esim Notepadilla) tekstitiedosto 'nimet.txt', 
# johon lisäät vähintään kymmenen naisten ja kymmenen miesten etunimeä.
#Tee ohjelma, joka lukee em. tekstitiedostosta nimet ja kertoo montako nimeä löytyy ja montako kertaa kukin nimi esiintyy.
#Huomioi myös muut mahdolliset poikkeukset joita tiedoston käsittely voi aiheuttaa.
lines = []
sama = ""
filename = "nimet.txt"
kertaa = 0
montako = 0
#path ="C:\Users\ella_\Desktop\JAMK\Ohjelmointi\ttc2030\nimet.txt"
try:
    file = open(path + filename, "r")
    lines = file.readlines()
    lines.sort()
#kertoo montako nimeä löytyy
    for nimi in lines:
        montako = montako + 1
        kertaa = lines.count(nimi)
        if nimi!=sama:
            print(nimi, end="Esiintymiskerrat: ")
            print(kertaa)
            sama = nimi

#montako kertaa kukin nimi esiintyy.
except:
    print("Failed to read file: " + filename)
finally:
    file.close()

#print(lines)
print(montako, "nimiä oli tiedostossa")

#Tehtävä L1503
#Jatkoa edelliseen. Lajittele nimet aakkosjärjestykseen ennen tulostusta.
lines = []
sama = ""
filename = "nimet.txt"
kertaa = 0
montako = 0
#path = "C:\Users\ella_\Desktop\JAMK\Ohjelmointi\ttc2030\nimet.txt"
try:
    file = open(filename, "r")
    lines = file.readlines()
    lines.sort()
    #ja kertoo montako nimeä löytyy
    for nimi in lines:
        montako = montako + 1
        kertaa = lines.count(nimi)
        if nimi!=sama:
            print(nimi, end="Esiintymiskerrat: ")
            print(kertaa)
            sama = nimi

#montako kertaa kukin nimi esiintyy.
except:
    print("Failed to read file: " + filename)
finally:
    file.close()

#print(lines)
print(montako, "nimiä oli tiedostossa")

#Tehtävä L1504
#Tee ohjelma joka kysyy käyttäjältä lukuja (joko kokonaisluku tai liukuluku) 
#ja tallenna kokonaisluvut eri tiedostoon kuin liukuluvut.
#Sovellus tulee lopettaa jos käyttäjä ei syötä kokonais- tai liukulukua.
#Tarkista tiedostojen sisältö tekstieditorilla.

while True:
    luku = input("Saisinko luvun?:")
    try:
        float(luku)
    except:
        #Sovellus tulee lopettaa jos käyttäjä ei syötä kokonais- tai liukulukua.
        break
    #Sovellus tulee lopettaa jos käyttäjä ei syötä kokonais- tai liukulukua.
    if luku == "":
        break
    #tallenna kokonaisluvut eri tiedostoon kuin liukuluvut.
    if luku == int:
        filename = "kokonaisluvut.txt"
        file = open(filename, "w")
        file.write(luku)
        file.close()  
    if luku == float:
        filenam = "liukuluvut.txt"
        file = open(filenam, "w")
        file.write(luku)
        file.close()
#Tarkista tiedostojen sisältö tekstieditorilla.

lines = []
try:
    file = open(filename, "r")
    lines = file.readlines()
    print(lines)
except:
    print("Failed to read")
finally:
    file.close()


# Tehtävä L1505
#Tee ohjelma, joka arpoo lottorivin ja tallentaa ne tekstitiedostoon 'lotto.txt'.
#Arvottu rivi sisältää seitsemän (7) numeroa väliltä 1-40. Varmista arpoessasi riviä että sama numero ei voi esiintyä kahta kertaa.
import os.path
import random
mypath = os.path.expanduser("~\\pythontesti")
if not os.path.exists(mypath):
    os.makedirs(mypath)


def lotto():
  indexes = [(i+1) for i in range(40)]
  numbers = []

  for x in range(7):
    index = random.randrange(0,len(indexes)-1)
    numbers.append(indexes[index])
    indexes.pop(index)
  
  #numbers.sort()
  string = ','.join(str(number) for number in numbers)
  return string

filename = "lotto.txt"
mypath += "\\"
file = open(mypath + filename, "w")
msg = "Lottoarvonnan numerot ovat: " + str(lotto())
file.write(msg)
file.close()
print(msg)

lotto()




