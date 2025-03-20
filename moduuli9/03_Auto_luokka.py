#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan
#tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella
#vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen
#kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa
#kuljetun matkan lukemaan 2090 km.

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

#Metodi2
    def kuljettu_matka(self, tunnit):
        self.matka += self.nykynopeus * tunnit

#Pääohjelma
auto = Auto("ABC-123", 142)
print(f"Auton rekisterinumero: {auto.rtunnus}")
print(f"Auton huippunopeus: {auto.huippunopeus} km/h")
print(f"Auton nykynopeus: {auto.nykynopeus}")
print(f"Auton kuljettu matka: {auto.matka} \n")

#Auton kiihdytys
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.nykynopeus} km/h")

#Tehdään vielä hätäjarrutus
auto.kiihdyta(-200)
print(f"Auton nopeus hätäjärrutuksen jälkeen: {auto.nykynopeus} km/h \n")

#Ajetaan autoa vaikka 3 tuntia
auto.kiihdyta(100) #Jarrutuksen jälkeen nopeus on 0, joten nostetaan sitä 100km
print(f"Kiihdytetään autoa taas jarrutuksen jälkeen {auto.nykynopeus} km/h")
auto.kuljettu_matka(3)
print(f"Auton kuljettu matka on ajon jälkeen on: {auto.matka} km")