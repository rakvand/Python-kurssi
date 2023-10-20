# Melko simppeli laskin-ohjelma

import math

def otaluku():
    while True:
        luku = input("Anna luku: ")

        try:
            luku = int(luku)
        except (TypeError, ValueError):
            print("Virheellinen syöte!")
        else:
            return luku

def main():
    luku1 = otaluku()
    luku2 = otaluku()

    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin (luku1/luku2)\n(6) cos (luku1/luku2)\n(7) Vaihda luvut\n(8) Lopeta")
        print("Valitut luvut:", luku1, luku2)

        valinta = input("Tee valinta (1-8): ")
        summa = luku1 + luku2
        erotus = luku1 - luku2
        tulo = luku1 * luku2
        osam = luku1 / luku2
        sini = math.sin(luku1/luku2)
        kosini = math.cos(luku1/luku2)

        if valinta == "8":
            break
        elif valinta == "1":
            print("Tulos on:", summa)
        elif valinta == "2":
            print("Tulos on:", erotus)
        elif valinta == "3":
            print("Tulos on:", tulo)
        elif valinta == "4":
            print("Tulos on:", osam)
        elif valinta == "5":
            print("Tulos on:", sini)
        elif valinta == "6":
            print("Tulos on:", kosini)
        elif valinta == "7":
            luku1 = otaluku()
            luku2 = otaluku()
            continue
        else:
            print("Valintaa ei tunnistettu.")

if __name__ == "__main__":
    main()