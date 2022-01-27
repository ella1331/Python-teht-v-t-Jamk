#tehtävä L10T01
#Tee funktio show_info, joka näyttää konsolissa tekstin "I'm Utils.Info"

def show_info():
   print("I'm Utils.Info")

show_info()

#L10T02
#Tee funktio subtract, jolle viedään 2 parametria. Funktion tulee palauttaa annettujen parametrien erotuksen.

def subtract(a,b):
    return a - b

print(subtract(1,2))

# L10T03
# Tee funktio average, jolle viedään 3 parametria. 
# Average funktio palauttaa annettujen parametrien keskiarvon yhden desimaalin tarkkuudella.   

def average(a, b, c):
   return round((a+b+c)/3, 1)

print(average(2,4,6))

#L10T04
#Tee funktio calc_consumption. Sinne viedään parametreina:

# -auton kulutus litraa/100km
# -polttoaineen hinta euroa per litra
# -kuljettu matka kilometreinä.
# -calc_consumption-funktio palauttaa tietoina kuinka monta litraa polttoainetta on kulunut matkalla 
#   sekä polttoaineeseen kuluneen rahan määrän. Kysy käyttäjältä: kulutus, polttoaineen hinta ja kuljettu matka. 
# -Sen jälkeen kutsu calc_consumption-funktiota ohjelmasta. Tarkista että funktio laskee kulutuksen ja polttoaineen hinnan oikein.

def calc_consumption():
    rivi = input("Enter trip length in km:")
    matka = float(rivi)
    rivi = input("Enter fuel price/liter:")
    hinta = float(rivi)
    rivi = input("Enter fuel consumption/100 km:")
    kulutus = float(rivi)
    kokonaiskulutus = (matka / 100) * kulutus
    maksu = ((kulutus/100) * matka)*hinta
    print("Fuel:" + "{:.2f}".format(kokonaiskulutus),"liter")
    print("Cost:" + "{:.2f}".format(maksu),"€")

calc_consumption()

