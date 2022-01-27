#Tehtävä L13T01 A
#Toteuta ohjelma, joka kysyy käyttäjältä autojen rekisterinumeroita (siis esim 'ABC-123' jne)
#ja tallentaa ne listaan. Käyttäjä voi syöttää niin monta rekisterinumeroa kuin haluaa, 
#syöttäminen lopetetaan tyhjällä syötteellä. Näytä syötetyt rekisterinumero aakkosjärjestyksessä.

def rekisteriKilvet():
    kilvet = []
    while True:
        syote = input("Anna rekisterinumero (esim. ABC-123): ")
        if len(syote) == 0:
            break
        kilvet.append(syote)
    return kilvet

rekisteri = rekisteriKilvet()
rekisteri.sort
print(rekisteri)

# Tehtävä L1302 A
# Tee ohjelma joka kysyy käyttäjältä kurssien arvosanoja 
# (arvosana on kokonaisuluku 0,1,2,3,4 tai 5) ja tallentaa ne listaan. 
# Käyttäjä voi syöttää niin monta kurssiarvosanaa kuin haluaa, syöttäminen lopetetaan tyhjällä syötteellä. 
# Näytä lopuksi montako arvosanaa käyttäjä antoi ja arvosanojen keskiarvo.
def arvoSanat():
    luvut = []
    while True:
        syote = input("Anna kurssin arvosana väliltä 0-5: ")
        if len(syote) == 0:
            break
        luvut.append(int(syote))
       
    return luvut

luvut = arvoSanat()
keskiarvo = sum (luvut)/ len(luvut)
print("Arvosanoja annettu:", len(luvut))
print("Arvosanojen keskiarvo", keskiarvo)

# Tehtävä L13T03
# Toteuta ohjelma, johon voi tallentaa kymmenen eri auton tiedot. 
# Kustakin autosta tiedetään rekisterinumero (esim ABC-123) ja autonmerkki (esim Skoda). 
# Keksi itse erilaisia rekisterinumeroita ja automerkkejä. Tallenna tiedot valitsemaasi kokoelmaan. 
# Tulosta sen jälkeen autojen tiedot ensin aakkosjärjestyksssä automerkin mukaan,
# ja sen jälkeen aakkosjärjestyksessä rekisterinumeron mukaan.

class Car:
    merkki = ""
    rekisteriTunnus = ""

    def __str__(self):
        return  self.merkki + " " + self.rekisteriTunnus

    def __init__(self,merkki="",rekisteriTunnus=""):
        self.merkki = merkki
        self.rekisteriTunnus = rekisteriTunnus


eka = Car("Skoda", "ABC-123")
toka = Car("Audi", "SDF-111")
kolmas = Car("Volvo", "FGT-456")
neljäs = Car("BMW", "IUT-999")
viides = Car("Ford", "EEE-777")
kuudes = Car("VW", "AAA-444")
seiska = Car("Mini", "HJK-369")
kasi = Car("Kia", "BRC-147")
ysi = Car("Huyndai", "LOL-951")
kymppi = Car("Lada", "JEE-555")

cars = [eka, toka, kolmas, neljäs, viides, kuudes, seiska, kasi, ysi, kymppi]
cars.sort(key=lambda cars:cars.merkki)
for cars in cars:
    print(cars.merkki, "-", cars.rekisteriTunnus) 

cars = [eka, toka, kolmas, neljäs, viides, kuudes, seiska, kasi, ysi, kymppi]
cars.sort(key=lambda cars:cars.rekisteriTunnus)
for cars in cars:
    print(cars.rekisteriTunnus, "-", cars.merkki)