from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        # Muutetaan luku kokonaisluvuksi
        luku = int(luku)

        # Testataan onko luku alkuluku
        if luku < 2:
            onko_alkuluku = False
        else:
            onko_alkuluku = True
            jakaja = 2
            while jakaja <= (luku // 2):
                if luku % jakaja == 0:
                    onko_alkuluku = False
                    break
                jakaja += 1

        tilakoodi = 200
        vastaus = {
            "Number": luku,  # Muutettu dynaamiseksi
            "isPrime": onko_alkuluku
        }

        return jsonify(vastaus), tilakoodi

    except:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "Teksti": "Virheellinen parametri"
        }
        return jsonify(vastaus), tilakoodi


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)