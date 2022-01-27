#Tehtävä L1401

#Tee ohjelma, jossa yrität muuttaa listan sellaista arvoa, jota ei ole olemassa.
#Alusta siis lista, jossa on neljä elementtiä ja sen jälkeen yritä muuttaa viidettä elementtiä.
try:
    lista = [1, 2, 3, 4]
    if lista[5] == "":
        print(lista)
#Tarkista millaisen poikkeuksen saat.   (list index out of range)
#Korjaa ohjelma niin ettei se kaadu.    
except IndexError:
    print("Value not on list")

#Tehtävä L1402
#Tee ohjelma, jolla yrität lukea Windows-koneella kaikki tiedostot kovalevyn C:n juuresta 
#Näytä tiedostot konsolilla. Koeta sen jälkeen lisätä tiedosto 'ayho.txt' C:n juureen.
#Mitä tapahtui? Korjaa ohjelma niin, ettei se kaadu.


from os import listdir
from os.path import isfile, join
filename = "files-example.txt"

tiedostot=[]

lines=listdir("C:\\")
for rivi in lines:
    if isfile("C:\\"+ rivi):
        tiedostot.append(rivi)
#Näytä tiedostot konsolilla.
print(tiedostot)

#Koeta sen jälkeen lisätä tiedosto 'ayho.txt' C:n juureen
try:
    file = open("C:\\" + filename, "w")
    file.write("ayho.txt")
    file.close()

#Mitä tapahtui? Korjaa ohjelma niin, ettei se kaadu.
except:
    print("Failed to create file to drive root")


#Bonuskysymys: Millä oikeuksilla voisit lisätä tiedostoja macOS/Linux/Unix-koneissa juurihakemistoon? Vastaus kommenttina lähdekoodiin.
# Vastaus: Pääkäyttäjänä

#Tehtävä L1403
# Mitä havaitset? Vastaukset tehtävän alkuun kommentteina.
# Sain sen toimimaan ohjeiden mukaisesti.


#Toteuta funktio isthiszero(num). Funktiolla välitetään yksi parametri. 
def isthiszero(num):
    #Funktio palauttaa true jos parametrin arvo on nolla.
    if num == 0:
        return True
    #Funktio palauttaa false, jos parametri on luku mutta ei nolla.
    if num > 0 or num < 0:
        return False
#Funktio nostaa TypeError-poikkeuksen, jos parametri ei ole luku. 
#Toteuta kutsuvalla ohjelmalle try - except.
try:       
    #Kokeile kutsua  ohjelmasta funktioita eri arvoilla.
    tulos = isthiszero(5) 
    print(tulos)
    tulos = isthiszero(0) 
    print(tulos)
    tulos = isthiszero("A") 
    print(tulos)
except TypeError:
    print("Anna vain lukuja")


#L1405
#Tee kokoelma, jossa on 5 merkkijonoa.
merkkijono = [1, 2, 3, 4, 5]
#Kysy käyttäjältä indeksi mihin kohtaan taulukkoa käyttäjä haluaa syöttää uuden tekstin.
teksti = int(input("Mihin kohtaan jonoa haluaisit tekstiä?(1-5):"))
#Kysy käyttäjältä uusi teksti ja laita se taulukkoon käyttäjän antamaan indeksiin.
uusiteksti = input("Minkä tekstin haluaisit lisätä?:")
    
if teksti == 1:
    merkkijono[0] = uusiteksti
    print(merkkijono)

if teksti == 2:
    merkkijono[1] = uusiteksti
    print(merkkijono)

if teksti == 3:
    merkkijono[2] = uusiteksti
    print(merkkijono)

if teksti == 4:
    merkkijono[3] = uusiteksti
    print(merkkijono)

if teksti == 5:
    merkkijono[4] = uusiteksti
    print(merkkijono)
#Korjaa ohjelma niin ettei se kaadu, jos käyttäjä syöttää indeksin, joka on taulukon ulkopuolella.
#Kerro käyttäjälle mikäli indeksi ei ole kelvollinen ja pyydä syöttämään se uudestaan.
if teksti >= 6:
    print("Annoit luvun joka ei ole listassa, anna luku 1-5")

