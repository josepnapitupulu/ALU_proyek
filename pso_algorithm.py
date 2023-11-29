import numpy as np

def hitung_jarak(x, y):
    return np.sqrt(np.sum((x - y)**2))

def PSO(n_partikel, n_iterasi, batas_bawah, batas_atas, tempat_asal, koordinat_tempat_asal, tempat_tujuan, koordinat_tempat_tujuan):
    dimensi = len(batas_bawah)

    posisi_tempat_asal = np.array([koordinat_tempat_asal[tempat_asal[0]]])

    posisi_partikel = np.random.uniform(batas_bawah, batas_atas, size=(n_partikel, dimensi))
    kecepatan_partikel = np.random.rand(n_partikel, dimensi)

    pbest = posisi_partikel.copy()
    fitness_pbest = np.array([hitung_jarak(pos, posisi_tempat_asal[0]) for pos in pbest])
    gbest_index = np.argmin(fitness_pbest)
    gbest = pbest[gbest_index].copy()

    inertia_weight = 0.8
    c1 = 1.5
    c2 = 1.5

    for iterasi in range(n_iterasi):
        fitness_partikel = np.array([hitung_jarak(pos, posisi_tempat_asal[0]) for pos in posisi_partikel])

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
        posisi_partikel = posisi_partikel + kecepatan_partikel
        posisi_partikel = np.clip(posisi_partikel, batas_bawah, batas_atas)

    tempat_terdekat_index = np.argmin([hitung_jarak(gbest, koordinat_tempat_tujuan[tempat]) for tempat in tempat_tujuan])
    tempat_terdekat = list(tempat_tujuan)[tempat_terdekat_index]

    total_jarak = hitung_jarak(gbest, koordinat_tempat_tujuan[tempat_terdekat])

    return gbest, total_jarak, tempat_terdekat
