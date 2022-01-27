# L07T01
#Tee ohjelma, joka tulostaa konsoliin tekstin "Here starts basics of programming with Python". Lisää toinen rivi, jossa on etunimesi ja sukunimesi välilyönnillä erotettuna, siis esim "Jakke Jäyhä".


print("Here starts basics of programming with Python")
print("Elina Luumi")

# L07T02
#Tee ohjelma, jossa käytät muuttujaa, johon tallennat henkilön pituuden kokonaisina senttimetreinä. Ohjelma tulostaa muuttujan arvo konsoliin.

pituus = 182
print(pituus)

#L07T03
#Tee ohjelma joka kysyy käyttäjältä kaksi kokonaislukua ja tulostaa niiden summan.

line = input("Anna kokonaisluku: ")
number = int(line)

line2 = input("Anna toinen kokonaisluku: ")
number2 = int(line2)

print("Summa:", number + number2)

number = 3
number2 = 5
print("Summa: ", number + number2)

#L07T04
#Tee ohjelma joka kysyy käyttäjältä kaksi kokonaislukua ja tulostaa niiden:

line3 = input("Anna kokonaisluku: ")
number3 = int(line3)

line4 = input("Anna toinen kokonaisluku: ")
number4 = int(line4)

print("Summa:", number3 + number4)
print("Erotus:", number3 - number4)
print("Tulo:", number3 * number4)
print("Osamäärä:", number3 / number4)


#L07T05
#Esittele muuttuja, johon tallennetaan pankkitilin saldo euroina (alku saldo on 2000 €). Tulosta pankkitilin saldo konsoliin. Kysy konsolissa kuinka monta euroa lisätään saldoon. Kysy konsolissa kuinka monta senttiä lisätään saldoon. Tulosta saldo konsoliin näiden muutosten jälkeen.

saldo = 2000
print("Bank account balance:",saldo, "€")

line5 = input("How many euros will be added to the balance? ")
number5 = int(line5)

line6 = input("How many cents will be added to the balance? ")
number6 = float(line6)
number6 = number6 / 100
print("Bank account balance:",saldo + number5 + number6, "€")