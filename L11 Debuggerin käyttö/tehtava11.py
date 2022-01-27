#Tehtävä L11T01
#Tee funktio time, joka muuttaa parametrinä saadun sekuntiarvon muotoon tunnit:minuutit:sekunnit. 
# Esimerkiksi luvulle 10000, palautetaan tieto seuraavassa muodossa "02:46:40"

#TÄMÄ EI ANNA IHAN TOIVOTTUA TAPAA!
from datetime import datetime, timedelta

def GetTime():
    sec = timedelta(seconds=int(input('Enter the number of seconds: ')))
    d = datetime(1,1,1) + sec

    print("%d:%d:%d" % (d.hour, d.minute, d.second))

GetTime()

#TÄMÄ ANTAA TOIVOTUN TAVAN, MUTTA TESTI EI HYVÄKSY SITÄ!
import time
  
def Time(seconds):
    
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

 
print(Time(10000))


import datetime
  
def time(line):
    return str(datetime.timedelta(seconds = line))

line = int(input("Anna sekunnit:"))  
print(time(line))

#TÄSSÄ TESTIIN OIKEA TAPA TEHDÄ:
def time(seconds):
    hrs = int(seconds / 3600)    
    mins = int(seconds % 3600 / 60)
    secs = int(seconds % 3600 % 60)


    if hrs < 10:
        hrs = "0"+ str(hrs)
    if mins < 10:
        mins = "0"+ str(mins)
    if secs < 10:
        secs = "0"+ str(secs) 
        
    return (str(hrs) + ":" + str(mins) + ":" + str(secs))

#Tehtävä L11T02
#Tee funktiot: celToFah ja fahToCel
#Funktiot ottavat parametrikseen asteluvun ja muuttavat sen joko fahrenheitit celsiuksiksi tai celsius-asteet fahrenheitiksi. 
# Muutettu astearvo palautetaan yhden desimaalin tarkkuudella.
#Testaa kumpikin funktio kutsumalla sitä käyttäjän antamilla luvuilla.
#Esimerkiksi testi print(celToFah(10.0)) palauttaa arvon 50.0

def celToFah(TCelsius):
    return (TCelsius * 9/5) + 32

def fahToCel(TFahren):
    return("{:.1f}".format((TFahren-32)/1.8))

print(celToFah(10))
print(fahToCel(50))

#Tehtävä L11T03
#Tee ohjelma, joka kysyy oppilaitten nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen.
#  Ohjelma kertoo tämän jälkeen montako nimeä annettiin ja näyttää ne yhtenä rivinä pilkulla erotettuna.

def oppilaiden_nimet():
    nimet = []
    while True:
        syote = input("Enter student name:")
        if len(syote) == 0:
            break
        nimet.append(syote)
    return nimet

nimet = oppilaiden_nimet()
print("Student count:", len(nimet))
nimet = ", ".join(nimet)
print(nimet)

#Tehtävä L11T04
#Mäkihypyssä käytetään viittä arvostelutuomaria. Kirjoita ohjelma, joka kysyy 
# arvostelupisteet yhdelle hypylle ja tulostaa tyylipisteiden summan siten, 
# että summasta on vähennetty pois pienin ja suurin tyylipiste.

def mäkihyppy():
    summa = []
    for x in range(5):
        line = int(input('Give points:'))
        summa.append(int(line))
    summa.remove(max(summa))
    summa.remove(min(summa))
    print("Total points are:",sum(summa))

mäkihyppy()
