class Auto:
    def __init__(self, tunnus, huippunopeus):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.matka = 0

auto = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus: {auto.tunnus}")
print(f"Auton huippunopeus: {auto.huippunopeus} km/h")
print(f"Auton tämänhetkinen nopeus: {auto.nykynopeus}")
print(f"Auton kuljettu matka: {auto.matka}")

