#Autokilpailu
import random

# Luokka Auto
class Auto:
    def __init__(self, rtunnus, huippunopeus):
        self.rtunnus = rtunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.matka = 0

    # Metodi (kiihdytys)
    def kiihdyta(self, muutos):
        self.nykynopeus += muutos
        if self.nykynopeus > self.huippunopeus:
            self.nykynopeus = self.huippunopeus
        elif self.nykynopeus < 0:
            self.nykynopeus = 0

    # Metodi (kuljettu matka)
    def kuljettu_matka(self, tunnit):
        self.matka += self.nykynopeus * tunnit

# Luodaan 10 autoa
autot = []
for x in range(1, 11):
    rekisteritunnus = f"ABC-{x}"
    huippunopeus_auto = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus_auto))

# Kilpailu alkaa
while True:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kuljettu_matka(1)
        if auto.matka >= 10000:
            # Jos joku auto saavuttaa 10 000 km, lopetetaan kilpailu
            print(f"{auto.rtunnus} voitti kilpailun! \n")
            break
    else:
        continue

    break

# Tulostetaan lopputulokset
print("Kilpailun lopputulokset:")
print("Rekisteritunnus | Huippunopeus | Nopeus | Kuljettu matka \n")
for auto in autot:
    print(f"{auto.rtunnus} | {auto.huippunopeus} km/h | {auto.nykynopeus} km/h | {auto.matka} km")
