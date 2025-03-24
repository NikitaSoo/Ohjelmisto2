class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self,nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")
        super().tulosta_tiedot()


class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(nimi)
        
    def tulosta_tiedot(self):
        print(f"Päätoimittaja: {self.toimittaja}")
        super().tulosta_tiedot()

aku = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti nro 6", "Rosa Likson,", 200)

aku.tulosta_tiedot()
print("")
kirja.tulosta_tiedot()