# kasir Terminal Bus Sidoarjo
jumlah = 0
total_pendapatan = 0
total_jarak = 0
terjauh = 0

while True:
    jarak = int(input("Masukkan jarak penumpang (km, 0 untuk selesai): "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid, silakan ulangi input!")
        continue

    jumlah += 1

    # menghitung tarif berdasarkan jarak
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    # diskon 50% untuk penumpang ke-5, ke-10, dan seterusnya
    if jumlah % 5 == 0:
        tarif = tarif // 2
        print("Penumpang ke-", jumlah, "mendapat diskon 50%")

    print("Tarif penumpang ke-", jumlah, ": Rp", tarif)

    total_pendapatan += tarif
    total_jarak += jarak
    if jarak > terjauh:
        terjauh = jarak

# rekap akhir
print("===== REKAP KASIR =====")
if jumlah > 0:
    print("Jumlah penumpang :", jumlah)
    print("Total pendapatan : Rp", total_pendapatan)
    print("Jarak terjauh    :", terjauh, "km")
    print("Rata-rata jarak  :", (total_jarak / jumlah, 2), "km")
else:
    print("Tidak ada penumpang yang dicatat")