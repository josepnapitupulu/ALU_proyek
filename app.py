from flask import Flask, render_template, request
import numpy as np
from pso_algorithm import PSO

app = Flask(__name__)

koordinat_tempat_asal = {
    "Asal_1": [5, 10],
    "Asal_2": [5, 10],
    "Asal_3": [5, 10],
    "Asal_4": [5, 10],
}

koordinat_tempat_tujuan = {
    "Kota_A": [20, 30],
    "Kota_B": [40, 50],
    "Kota_C": [60, 70],
    "Kota_D": [80, 90],
    "Kota_E": [5, 5],
    "Kota_F": [39, 35],
    "Kota_G": [20, 45],
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tempat_asal = list(koordinat_tempat_asal.keys())
        tempat_tujuan = list(koordinat_tempat_tujuan.keys())

        n_partikel = 50
        n_iterasi = 100
        batas_bawah = [0, 0]
        batas_atas = [100, 100]

        solusi_terbaik, jarak_terbaik, tempat_terdekat = PSO(
            n_partikel, n_iterasi, batas_bawah, batas_atas, tempat_asal,
            koordinat_tempat_asal, tempat_tujuan, koordinat_tempat_tujuan
        )


        return render_template('index.html', solusi_terbaik=solusi_terbaik.tolist(),
                               jarak_terbaik=jarak_terbaik, tempat_terdekat=tempat_terdekat)

    tempat_asal = list(koordinat_tempat_asal.keys())
    tempat_tujuan = list(koordinat_tempat_tujuan.keys())
    return render_template('index.html', tempat_asal=tempat_asal, tempat_tujuan=tempat_tujuan)

if __name__ == '__main__':
    app.run(debug=True)
