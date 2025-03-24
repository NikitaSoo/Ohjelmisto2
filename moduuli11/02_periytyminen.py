class Auto:
    def __init__(self, rtunnus, huippunopeus):
        self.rtunnus = rtunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nykynopeus += muutos
        if self.nykynopeus > self.huippunopeus:
            self.nykynopeus = self.huippunopeus
        elif self.nykynopeus < 0:
            self.nykynopeus = 0

    def kuljettu_matka(self, tunnit):
        self.matka += self.nykynopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rtunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rtunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rtunnus, huippunopeus, bensatankki):
        super().__init__(rtunnus, huippunopeus)
        self.bensatankki = bensatankki

# Pääohjelma
e_auto = Sahkoauto("ABC-15", 180, 52.5)
p_auto = Polttomoottoriauto("ACD-123", 165, 32.3)

e_auto.kiihdyta(120)
p_auto.kiihdyta(140)

e_auto.kuljettu_matka(3)
p_auto.kuljettu_matka(3)

print(f"Sähköauton ({e_auto.rtunnus}) matkamittarilukema: {e_auto.matka} km")
print(f"Polttomoottoriauton ({p_auto.rtunnus}) matkamittarilukema: {p_auto.matka} km")
