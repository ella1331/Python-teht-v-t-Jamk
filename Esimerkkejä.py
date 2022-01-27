#Esimerkkejä
import os.path
import datetime

#haetaan käyttäjän kotihakemisto
mypath = os.path.expanduser("~")
print("Käyttäjän kotihakemisto on ", mypath)

# luodaan uusi kansio kotihakemistoon
mypath = os.path.expanduser("~\\pythontesti")
if not os.path.exists(mypath):
    os.makedirs(mypath)

# luodaan tiedosto
filename = "testifile.txt"
mypath += "\\"
file = open(mypath + filename, "w")
msg = "Tiedosto " + filename + " luotu onnistuneesti " + str(datetime.datetime.now())
file.write(msg)
file.close()
print(msg)

#Nämä oli harjoittelua L15 tehtävään

filename = "kokonaisluvut.txt"
mypath += "\\"
file = open(mypath + filename, "w")
file.close()

filename = "liukuluvut.txt"
mypath += "\\"
file = open(mypath + filename, "w")
file.close()