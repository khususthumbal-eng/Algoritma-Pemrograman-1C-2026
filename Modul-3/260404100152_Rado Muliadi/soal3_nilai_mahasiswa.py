# pengelolaan nilai 10 mahasiswa
jumlah_a = jumlah_b = jumlah_c = jumlah_d = jumlah_e = 0
total_akhir = 0
tertinggi = -1
terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print("Mahasiswa ke-" + str(i))
    nama = input("Nama        : ")
    tugas = float(input("Nilai tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    # nilai akhir dengan bobot 30% : 30% : 40%
    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    # menentukan kategori nilai
    if akhir >= 85:
        kategori = "A"
        jumlah_a += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_b += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_c += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_d += 1
    else:
        kategori = "E"
        jumlah_e += 1

    print("Hasil", nama, "| T=", tugas, "UTS=", uts, "UAS=", uas, "| Akhir=", akhir, "|", kategori)

    total_akhir += akhir
    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

# rekap setelah semua data diproses
print("===== REKAP KELAS =====")
print("Jumlah nilai A :", jumlah_a)
print("Jumlah nilai B :", jumlah_b)
print("Jumlah nilai C :", jumlah_c)
print("Jumlah nilai D :", jumlah_d)
print("Jumlah nilai E :", jumlah_e)
print("Nilai akhir tertinggi", ":", tertinggi, "(", nama_tertinggi, ")")
print("Nilai akhir terendah  :", terendah, "(", nama_terendah, ")")
print("Rata-rata nilai akhir :", total_akhir / 10)