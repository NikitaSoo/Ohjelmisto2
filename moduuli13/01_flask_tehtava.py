from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:

        #Muutetaan kokonaisluvuksi
        luku = int(luku)

        #Testataan onko luku kokonaisluku
        onko_alkuluku = True
        jakaja = 2
        while jakaja < (luku // 2):
            if luku % jakaja == 0:

                onko_alkuluku = False
                break
            jakaja += 1

        tilakoodi = 200
        vastaus = {
            "Number": 31,
            "isPrime": onko_alkuluku
        }

    except:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "Teksti": "Virheellinen parametri"
        }



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)