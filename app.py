from flask import Flask, render_template, request
import numpy as np
from pso_algorithm import PSO

app = Flask(__name__)

koordinat_tempat_asal = {
    "Balige Pusat Kantor": {
        "Balige": [2.334655, 99.083166],
        "Ajibata": [2.609101, 98.946025],
        "Bonatua Lunasi": [2.525796, 99.115753],
        "Borbor": [2.201029, 99.266624],
        "Habinsaran": [2.310248, 99.336949],
        "Laguboti": [2.3832665, 99.1486140],
        "Lumban julu": [2.5767369, 99.0603619],
        "Nassau": [2.2736008, 99.4038087],
        "Parmaksian": [2.497967, 99.201461],
        "Pintu Pohan Meranti": [2.553819, 99.304101],
        "Porsea": [2.490482, 99.135669],
        "Siantar Narumonda": [2.490482, 99.135669],
        "Sigumpar": [2.399100, 99.199241],
        "Silaen": [2.439718, 99.288264],
        "Tampahan": [2.311486, 99.012720],
        "Uluan": [2.462616, 99.070699],
    },
}

koordinat_tempat_tujuan = {
    "Ajibata": {
        "Ajibata": [2.609101, 98.946025],
    },
    "Bonatua Lunasi": {
        "Bonatua Lunasi": [2.525796, 99.115753],
    },
    "Borbor": {
        "Borbor": [2.201029, 99.266624],
    },
    "Habinsaran": {
        "Habinsaran": [2.310248, 99.336949],
    },
    "Laguboti": {
        "Laguboti": [2.3832665, 99.1486140],
    },
    "Lumban julu": {
        "Lumban julu": [2.5767369, 99.0603619],
    },
    "Nassau": {
        "Nassau": [2.2736008, 99.4038087],
    },
    "Parmaksian": {
        "Parmaksian": [2.497967, 99.201461],
    },
    "Pintu Pohan Meranti": {
        "Pintu Pohan Meranti": [2.553819, 99.304101],
    },
    "Porsea": {
        "Porsea": [2.490482, 99.135669],
    },
    "Siantar Narumonda": {
        "Siantar Narumonda": [2.490482, 99.135669],
    },
    "Sigumpar": {
        "Sigumpar": [2.399100, 99.199241],
    },
    "Silaen": {
        "Silaen": [2.439718, 99.288264],
    },
    "Tampahan": {
        "Tampahan": [2.311486, 99.012720],
    },
    "Uluan": {
        "Uluan": [2.462616, 99.070699],
    },
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

        lokasi_asal = request.form['lokasi_asal']
        lokasi_tujuan = request.form['lokasi_tujuan']

        solusi_terbaik, total_jarak, tempat_terdekat, rute_terbaik= PSO(
            n_partikel, n_iterasi, batas_bawah, batas_atas,
            koordinat_tempat_asal, koordinat_tempat_tujuan,
            lokasi_asal, lokasi_tujuan
        )

        return render_template('index.html', solusi_terbaik=solusi_terbaik.tolist(),
                               total_jarak=total_jarak, tempat_terdekat=tempat_terdekat, rute_terbaik=rute_terbaik)

    tempat_asal = list(koordinat_tempat_asal.keys())
    tempat_tujuan = list(koordinat_tempat_tujuan.keys())
    return render_template('index.html', tempat_asal=tempat_asal, tempat_tujuan=tempat_tujuan)

if __name__ == '__main__':
    app.run(debug=True)