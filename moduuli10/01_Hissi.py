#Hissi

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
        #Aloitetaan hissi alimmassta kerroksesta

#Metodi ylös
    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

#Metodi alas
    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

# Pääohjelma
h = Hissi(1, 10)  # Luodaan hissi, joka liikkuu kerrosten 1 ja 10 välillä
h.siirry_kerrokseen(5)#Siirretään hissi viidenteen kerrokseen
print("")
h.siirry_kerrokseen(1)#Siirretään hissi takaisin alimpaan kerrokseen
