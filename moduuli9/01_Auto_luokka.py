#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
#huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
#Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin
#mainittua parametreina saatuihin arvoihin. Uuden auton nopeus ja
#kuljetut matka on asetettava automaattisesti nollaksi.
#Kirjoita pääohjelma, jossa luot uuden auton
#(rekisteritunnus ABC-123, huippunopeus 142 km/h).
#Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.


class Auto:
    def __init__(self, rtunnus, huippunopeus):
        self.rtunnus = rtunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.matka = 0

auto = Auto("ABC-123", 142)

print(f"Auton rekisterinumero: {auto.rtunnus}")
print(f"Auton huippunopeus: {auto.huippunopeus} km/h")
print(f"Auton nykynopeus: {auto.nykynopeus}")
print(f"Auton kuljettu matka: {auto.matka}")

