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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []
        i = 0
        while i < hissien_maara:
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))
            i += 1

    def aja_hissia(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohde_kerros}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virheellinen hissin numero.")

# Pääohjelma
talo = Talo(1, 10, 3)  # Luodaan talo, jossa on 3 hissiä

talo.aja_hissia(0, 5)  # Ajetaan ensimmäinen hissi viidenteen kerrokseen
talo.aja_hissia(1, 8)  # Ajetaan toinen hissi kahdeksanteen kerrokseen
talo.aja_hissia(2, 3)  # Ajetaan kolmas hissi kolmanteen kerrokseen
talo.aja_hissia(0, 1)  # Palautetaan ensimmäinen hissi takaisin alimpaan kerrokseen
