#Tehtävä L09T01
#Tee ohjelma, joka kysyy käyttäjältä viikon kunkin päivän sademäärän. 
# Sademäärä annetaan kokonaislukuna, jollei kyseisenä päivänä ole satanut käyttäjä antaa luvuksi 0. 
# Laske ja näytä viikon kokonaissademäärä.

summa = 0
for x in range(7):
    num = int(input('Anna viikon kunkin päivän sademäärä: '))
    summa = summa + num
print("Sademäärän summa on:",summa)

#Tehtävä L09T02
#Tee ohjelma, joka kysyy käyttäjältä kokonaislukuja. Lukuja kysytään siihen saakka kunnes käyttäjä antaa tyhjän syötteen.
#Laske kuinka monta lukua käyttäjä antoi, laske myös annettujen lukujen summa. Näytä annettujen lukujen lukumäärä ja summa käyttäjälle.

def main():
    lukujen_maara = 0
    summa = 0
    rivi = input("Anna luku: ")
    while rivi != "":
        luku = int(rivi)
        summa = summa + luku
        lukujen_maara = lukujen_maara + 1
        rivi = input("Anna luku: ")
    
    print("Lukuja annettu:", lukujen_maara)
    print("Lukujen summa:", summa)

main()


def lue_luvut():
    luvut = []
    while True:
        syote = input("Anna luku: ")
        if len(syote) == 0:
            break
        luvut.append(int(syote))
    return luvut

luvut = lue_luvut()
print("Lukuja annettu:", len(luvut))
print("Lukujen summa:", sum(luvut))


#Tehtävä l09T03
#Tee ohjelma, joka kysyy ensin käyttäjältä jonkin luvun väliltä 1-10.
#Tämän jälkeen näytä luvut yhdestä annettuun lukuun ja luvun neliön.

line = int(input("Anna numero väliltä 1-10: "))
for i in range(line):
    print("Luvun", i+1, "neliö on", (i+1) * (i+1))

#Tehtävä L09T04
#Tee ohjelma, joka kysyy käyttäjältä käyttäjän etu ja sukunimen. 
# Tulosta käyttäjän etunimen ensimmäistä kirjainta niin monta kertaa kun etunimessä on kirjaimia. 
# Tämän jälkeen tulosta käyttäjän sukunimi käänteisessä järjestyksessä.

etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")
print(etunimi[0]*len(etunimi), sukunimi[::-1] )

#Tehtävä L09T05
#Tee funktio lotto(), 
# joka arpoo lottorivin seitsemän (7) numeroa väliltä 1-40 ja palauttaa sen merkkijonona, luvut eroteltuna pilkuilla. 

from random import randint

rivi = []
while len(rivi) < 7:
    uusi = randint(1, 40)
    if uusi not in rivi:
        rivi.append(uusi)
merkkijono = "".join(map(str,rivi))         #TÄMÄ MUUTTAA MERKKIJONOKSI, MUTTA EI HALUTTUUN MUOTOON.
print(merkkijono)


#Lotto toisella tapaa
from random import shuffle

kaikki = list(range(1, 41))
shuffle(kaikki)
rivi = kaikki[0:7]
print(rivi)

#Ja vielä kolmannella tapaa: NÄMÄ EIVÄT TULOSTA MERKKIJONOA!
from random import sample

kaikki_luvut = list(range(1, 41))
rivi = sample(kaikki_luvut, 7)
print(rivi)

#versio kokeeseen ! KOKEESEEN VAIN EKA FUNKTIO !
import random
lottoNumerot = []
#listassa on 40 alkiota joiden arvo aluksi False
def arvonta():
    for i in range (40):
        lottoNumerot.append(False)
    #arvotaan 7 toisistaan poikkeavaa numeroa
    i = 0    #laskuri
    while i < 7:
        a = random.randrange(0,40)
        #tarkista onko listassa jo arvottu numero
        if not lottoNumerot[a]:
            lottoNumerot[a] = True      #muutetaan arvoon True
            i += 1
    
def tulosta_numerot():
    txt = ""
    i = 0
    for x in lottoNumerot:
        i += 1
        if x:
            txt += str(i) + ", "
    #tulostus samalle riville
    print(txt)

#pääohjelma
#kutsutaan funktioita
arvonta()
tulosta_numerot()

#Tenttiin oikea koodi
import random

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


