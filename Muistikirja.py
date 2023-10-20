# Tiedostojen käsittelyä muistio-ohjelmalla

import time

try:
    muistikirja = open("muistio.txt", "r")
    muistikirja.close()
except IOError:
    print("Oletusmuistiota ei löydy, luodaan tiedosto.")
    muistikirja = open("muistio.txt", "w")

while True:
    nykyinen_muistio = muistikirja.name
    print("Käytetään muistiota:", nykyinen_muistio)
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta\n")
    toiminto = input("Mitä haluat tehdä?: ")

    if toiminto == "1":
        muistikirja = open(nykyinen_muistio, "r")
        sisalto = muistikirja.read()
        print(sisalto)
        muistikirja.close()
    elif toiminto == "2":
        merkinta = input("Kirjoita uusi merkintä: ")
        muistikirja = open(nykyinen_muistio, "a")
        muistikirja.write(merkinta + ":::" + time.strftime("%X %x") + "\n")
        muistikirja.close()
    elif toiminto == "3":
        muistikirja = open(nykyinen_muistio, "w")
        muistikirja.close()
        print("Muistio tyhjennetty.")
    elif toiminto == "4":
        muistionimi = input("Anna tiedoston nimi: ")
        try:
            muistikirja = open(muistionimi, "r")
        except IOError:
            print("Tiedostoa ei löydy, luodaan tiedosto.")
            muistikirja = open(muistionimi, "w")

    elif toiminto == "5":
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta.")