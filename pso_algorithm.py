# # pso_algorithm.py

import numpy as np

def hitung_jarak(x, y):
    if isinstance(x, dict):
        x = np.array(list(x.values())[0])
    if isinstance(y, dict):
        y = np.array(list(y.values())[0])

    return round(np.sqrt(np.sum((x - y)**2)), 2)

def PSO(n_partikel, n_iterasi, batas_bawah, batas_atas, koordinat_tempat_asal, koordinat_tempat_tujuan, lokasi_asal, lokasi_tujuan):
    dimensi = len(batas_bawah)

    if not isinstance(koordinat_tempat_asal, dict) or not isinstance(koordinat_tempat_tujuan, dict):
        raise ValueError("koordinat_tempat_asal dan koordinat_tempat_tujuan harus berupa dictionary")

    tempat_asal = list(koordinat_tempat_asal.keys())
    tempat_tujuan = list(koordinat_tempat_tujuan.keys())

    posisi_tempat_asal = np.array(koordinat_tempat_asal[lokasi_asal][list(koordinat_tempat_asal[lokasi_asal].keys())[0]])

    posisi_partikel = np.random.uniform(batas_bawah, batas_atas, size=(n_partikel, dimensi))
    kecepatan_partikel = np.random.rand(n_partikel, dimensi)

    pbest = posisi_partikel.copy()
    fitness_pbest = np.array([hitung_jarak(pos, posisi_tempat_asal) for pos in pbest])
    gbest_index = np.argmin(fitness_pbest)
    gbest = pbest[gbest_index].copy()

    inertia_weight = 0.8
    c1 = 1.5
    c2 = 1.5
    
    rute_terbaik = []

    for iterasi in range(n_iterasi):
        fitness_partikel = np.array([hitung_jarak(pos, posisi_tempat_asal) for pos in posisi_partikel])

        mask_update_pbest = fitness_partikel < fitness_pbest
        pbest[mask_update_pbest] = posisi_partikel[mask_update_pbest]
        fitness_pbest[mask_update_pbest] = fitness_partikel[mask_update_pbest]

        gbest_index = np.argmin(fitness_pbest)
        gbest = pbest[gbest_index].copy()

        r1, r2 = np.random.rand(n_partikel, dimensi), np.random.rand(n_partikel, dimensi)
        kecepatan_partikel = (
            inertia_weight * kecepatan_partikel +
            c1 * r1 * (pbest - posisi_partikel) +
            c2 * r2 * (gbest - posisi_partikel)
        )

        # Perbaikan: Ambil kota-kota dari daerah yang dipilih
        daerah_dipilih = [tempat_asal[int(index)] for index in gbest if 0 <= int(index) < len(tempat_asal)]
        kota_dari_daerah_dipilih = []
        for daerah in daerah_dipilih:
            if isinstance(daerah, str):
                # Perbaikan: Handle jika daerah adalah string (bukan dictionary)
                kota_dari_daerah_dipilih.append(daerah)
            else:
                kota_dari_daerah_dipilih.extend(daerah['kota'])
            
        jumlah_kota_yang_diambil = min(len(kota_dari_daerah_dipilih), 3)
        kota_yang_diambil = np.random.choice(kota_dari_daerah_dipilih, jumlah_kota_yang_diambil, replace=False)

        # Perbaikan: Update rute_terbaik pada setiap iterasi
        rute_terbaik = [lokasi_asal] + [list(koordinat_tempat_asal[lokasi_asal].keys())[0]]
        for kota_index in kota_yang_diambil:
            rute_terbaik.extend([kota_index] if isinstance(kota_index, str) else tempat_asal[kota_index]['kota'])

        # Perbaikan: Hentikan iterasi jika kota tujuan sudah tercapai
        if lokasi_tujuan in rute_terbaik:
            break
            
        posisi_partikel = posisi_partikel + kecepatan_partikel
        posisi_partikel = np.clip(posisi_partikel, batas_bawah, batas_atas)

    tempat_terdekat_index = np.argmin([hitung_jarak(gbest, koordinat_tempat_tujuan[tempat][list(koordinat_tempat_tujuan[tempat].keys())[0]]) for tempat in tempat_tujuan])
    tempat_terdekat = tempat_tujuan[tempat_terdekat_index]

    total_jarak = hitung_jarak(gbest, koordinat_tempat_tujuan[tempat_terdekat][list(koordinat_tempat_tujuan[tempat_terdekat].keys())[0]])

    return gbest, total_jarak, tempat_terdekat, rute_terbaik

# 
# # pso_algorithm.py

# import numpy as np

# def hitung_jarak(x, y):
#     if isinstance(x, dict):
#         x = np.array(list(x.values())[0])
#     if isinstance(y, dict):
#         y = np.array(list(y.values())[0])

#     return round(np.sqrt(np.sum((x - y)**2)), 2)

# def PSO(n_partikel, n_iterasi, batas_bawah, batas_atas, koordinat_tempat_asal, koordinat_tempat_tujuan, lokasi_asal, lokasi_tujuan):
#     dimensi = len(batas_bawah)

#     if not isinstance(koordinat_tempat_asal, dict) or not isinstance(koordinat_tempat_tujuan, dict):
#         raise ValueError("koordinat_tempat_asal and koordinat_tempat_tujuan should be dictionaries")

#     tempat_asal = list(koordinat_tempat_asal.keys())
#     tempat_tujuan = list(koordinat_tempat_tujuan.keys())

#     posisi_tempat_asal = np.array(koordinat_tempat_asal[lokasi_asal][list(koordinat_tempat_asal[lokasi_asal].keys())[0]])

#     posisi_partikel = np.random.uniform(batas_bawah, batas_atas, size=(n_partikel, dimensi))
#     kecepatan_partikel = np.random.rand(n_partikel, dimensi)

#     pbest = posisi_partikel.copy()
#     fitness_pbest = np.array([hitung_jarak(pos, posisi_tempat_asal) for pos in pbest])
#     gbest_index = np.argmin(fitness_pbest)
#     gbest = pbest[gbest_index].copy()

#     inertia_weight = 0.8
#     c1 = 1.5
#     c2 = 1.5
    
#     rute_terbaik = []

#     for iterasi in range(n_iterasi):
#         fitness_partikel = np.array([hitung_jarak(pos, posisi_tempat_asal) for pos in posisi_partikel])

#         mask_update_pbest = fitness_partikel < fitness_pbest
#         pbest[mask_update_pbest] = posisi_partikel[mask_update_pbest]
#         fitness_pbest[mask_update_pbest] = fitness_partikel[mask_update_pbest]

#         gbest_index = np.argmin(fitness_pbest)
#         gbest = pbest[gbest_index].copy()

#         r1, r2 = np.random.rand(n_partikel, dimensi), np.random.rand(n_partikel, dimensi)
#         kecepatan_partikel = (
#             inertia_weight * kecepatan_partikel +
#             c1 * r1 * (pbest - posisi_partikel) +
#             c2 * r2 * (gbest - posisi_partikel)
#         )
#         daerah_dipilih = [tempat_asal[int(index)] for index in gbest if 0 <= int(index) < len(tempat_asal)]

#         # Ambil kota-kota dari daerah yang dipilih
#         kota_dari_daerah_dipilih = []
#         for daerah in sorted(daerah_dipilih, key=lambda x: x['nilai']):
#             kota_dari_daerah_dipilih.extend(daerah['kota'])
            
#         jumlah_kota_yang_diambil = min(len(kota_dari_daerah_dipilih), 3)  # Ganti dengan jumlah yang sesuai
#         kota_yang_diambil = np.random.choice(kota_dari_daerah_dipilih, jumlah_kota_yang_diambil, replace=False)

#         rute_terbaik = [lokasi_asal] + [list(koordinat_tempat_asal[lokasi_asal].keys())[0]]
#         for kota_index in kota_yang_diambil:
#             kota = tempat_asal[kota_index]['kota']
#             rute_terbaik.extend(kota)
            
#         posisi_partikel = posisi_partikel + kecepatan_partikel
#         posisi_partikel = np.clip(posisi_partikel, batas_bawah, batas_atas)

#     tempat_terdekat_index = np.argmin([hitung_jarak(gbest, koordinat_tempat_tujuan[tempat][list(koordinat_tempat_tujuan[tempat].keys())[0]]) for tempat in tempat_tujuan])
#     tempat_terdekat = tempat_tujuan[tempat_terdekat_index]

#     total_jarak = hitung_jarak(gbest, koordinat_tempat_tujuan[tempat_terdekat][list(koordinat_tempat_tujuan[tempat_terdekat].keys())[0]])

#     return gbest, total_jarak, tempat_terdekat, rute_terbaik