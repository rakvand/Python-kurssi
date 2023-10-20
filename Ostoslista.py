# Ostoslista-ohjelma, jossa käyttäjä voi lisätä tuotteita listaan, poistaa tuotteita listalta tai lopettaa.

lista = []

while True:
    valinta = input("Haluatko\n(1)Lisätä listaan\n(2)Poistaa listalta vai\n(3)Lopettaa?: ")

    if valinta == "1":
        syote = input("Mitä lisätään?: ")
        lista.append(syote)  # lisätään listan viimeiseksi alkioksi
    elif valinta == "2":
        print("Listalla on",len(lista),"alkiota.")
        poisto = int(input("Monesko niistä poistetaan?: "))  # 1. alkio on 0
        # virheenkäsittely ja ilmoitus jos käyttäjä valitsee poistettavan alkion listan ulkopuolelta
        try:
            lista.pop(poisto)
        except IndexError:
            print("Virheellinen valinta.")
    # lopetus ja listan tulostus allekkain
    elif valinta == "3":
        print("Listalla oli tuotteet:")
        for i in lista:
            print(i)
        break
    else:
        print("Virheellinen valinta.")