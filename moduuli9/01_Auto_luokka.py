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

