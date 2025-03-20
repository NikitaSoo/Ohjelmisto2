#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
#joka saa parametrinaan nopeuden muutoksen (km/h).
#Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava
#auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta
#suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
#että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
#Tulosta tämän jälkeen auton nopeus.
#Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
#Kuljettua matkaa ei tarvitse vielä päivittää.

#Clässi
class Auto:
    def __init__(self, rtunnus, huippunopeus):
        self.rtunnus = rtunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.matka = 0

#Metodi
    def kiihdyta(self, muutos):
        self.nykynopeus += muutos
        if self.nykynopeus > self.huippunopeus:
            self.nykynopeus = self.huippunopeus
        elif self.nykynopeus < 0:
            self.nykynopeus = 0

#Pääohjelma
auto = Auto("ABC-123", 142)
print(f"Auton rekisterinumero: {auto.rtunnus}")
print(f"Auton huippunopeus: {auto.huippunopeus} km/h")
print(f"Auton nykynopeus: {auto.nykynopeus}")
print(f"Auton kuljettu matka: {auto.matka}")

#Auton kiihdytys
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.nykynopeus} km/h")

#Tehdään vielä hätäjarrutus
auto.kiihdyta(-200)
print(f"Auton nopeus hätäjärrutuksen jälkeen: {auto.nykynopeus} km/h")