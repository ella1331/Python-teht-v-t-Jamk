#Tehtävä L12T01
#Tee luokka Human. Luokalla on kaksi ominaisuutta name ja age. Kirjoita Human-luokka seuraavasti:
#Konstruktori alustaa Human-olion nimen ja iän parametrien kautta.
#Luokan str metodi toimii kuten on alla esitetty

class Human:
    name = ""
    age = ""

    def näytä_info(self):
        msg = "Nimi:" + self.name + ", Ikä:" + self.age
        return msg

ihminen = Human()
ihminen.name = "Adam" 
ihminen.age = "18"

print(ihminen.näytä_info())

ihminen = Human()
ihminen.name = "Eva"
ihminen.age = "18"

print(ihminen.näytä_info())

#TENTTIIN:
class Human:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return self.name + " " + str(self.age)

first_human = Human("Adam", 18)
second_human = Human("Eve", 18)

#Tehtävä L12T02
#Tee luokka Cat. Tee Cat-luokalle kaksi ominaisuutta name ja color, 
# sekä yksi metodi miau. Luo Cat-luokasta kaksi erilaista kissa-oliota seuraavilla tiedoilla:
#name: Kit, color: black
#name: Kat, color: white
#Kissat sanovat naukuessaan: Meoooooow!
#Näytä kissa-olioiden ominaisuudet konsolille, laita kissat myös naukumaan:

class Kissa:
    name = ""
    color = ""

    def näytä(self):
        msg = self.name + ", Color: " + self.color
        return msg

    def mauku(miau):
        viesti = miau.name + " says: Meoooooow!" 
        return viesti

kissat = Kissa()
kissat.name = "Kit"
kissat.color = "black"
print(kissat.näytä())

kissat = Kissa()
kissat.name = "Kat"
kissat.color = "white"
print(kissat.näytä())

kissat = Kissa()
kissat.name = "Kit"
print(kissat.mauku())

kissat = Kissa()
kissat.name = "Kat"
print(kissat.mauku())

#Tehtävä L12T03
#Autotallissasi on kolme autoa. Tee luokka Car. 
# Tee luokalla on kolme ominaisuutta brand, model ja price. 
# Luo Car-luokasta vähintään kolme erilaista auto-oliota. Aseta autojen ominaisuudet seuraavasti:
# 1.brand="Skoda" model="Octavia" price=3000
# 2.brand="Audi" model="A4" price=4000
# 3.brand="Volvo" model="V70" price=5000

class Car:
    brand = ""
    model = ""
    price = 0

    def __str__(self):
        return  self.brand + " " + self.model + " " + str(self.price)

    def __init__(self,brand="",model="", price=0):
        self.brand=brand
        self.model=model
        self.price=price

eka = Car("Skoda", "Octavia", 3000)
toka = Car("Audi", "A4", 4000)
kolmas = Car("Volvo", "V70", 5000)

print("car1:", eka)
print("car2:", toka)
print("car3:", kolmas)

summa = eka.price + toka.price + kolmas.price
print("Total price of the cars is",summa)


#Tehtävä L12T04
#Tee edellisen tehtävän Car-luokkaa apuna käyttäen seuraava:
#Luo vähintään viisi erilaista auto-oliota seuraavista automerkeistä
#(brand) 'Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo' ja 'VW'. 
#Autojen model ominaisuuden voit jättää halutessasi tyhjäksi.
#Generoi satunnaisesti niille hinta väliltä 1000-10000.
# Lisää luodut auto-oliot cars-nimiseen list-rakenteeseen. Huom! Käytä apuna randint-funktiota satunnaisuuden toteuttamisessa.
from random import randint

class Car:
    brand = ""
    model = ""
    price = 0

    def __str__(self):
        return  self.brand + " " + self.model + " " + str(self.price)

    def __init__(self,brand="",model="", price=randint(1000,10000)):
        self.brand=brand
        self.model=model
        self.price=price


eka = Car("Skoda")
toka = Car("Audi")
kolmas = Car("Volvo")
neljäs = Car("BMW")
viides = Car("Ford")

cars = [eka, toka, kolmas, neljäs, viides]
for obj in cars:
    print(obj.brand, obj.price)         #NYT HINTA ON KAIKILLA AUTOILLA SAMA!


#TENTTIIN:
from random import *

class Car:
  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price

  def __str__(self):
    return self.brand + " " + self.model + " " + str(self.price)


car_brands = ['Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo', 'VW']
cars = []

for i in range(5):
    rand = randint(0, len(car_brands) - 1)
    brand = car_brands[rand]
    cars.append(Car(brand, "", randint(1000, 10000)))

