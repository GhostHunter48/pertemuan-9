def hitung_selisih(j1, m1, d1, j2, m2, d2):
    start = j1 * 3600 + m1 * 60 + d1
    end = j2 * 3600 + m2 * 60 + d2
    selisih = end - start

    jam = selisih // 3600
    menit = (selisih % 3600) // 60
    detik = selisih % 60

    return f"{jam} jam - {menit} menit - {detik} detik"

mulai_jam, mulai_menit, mulai_detik = 8, 10, 20
selesai_jam, selesai_menit, selesai_detik = 9, 15, 30

hasil = hitung_selisih(mulai_jam, mulai_menit, mulai_detik, selesai_jam, selesai_menit, selesai_detik)
print("Selisih waktu:", hasil)
