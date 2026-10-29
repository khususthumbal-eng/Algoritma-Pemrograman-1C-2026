# seleksi awal beasiswa
penuh = 0
sebagian = 0
tidak_dapat = 0
tidak_memenuhi = 0
diproses = 0

for i in range(1, 11):
    print("Mahasiswa ke-" + str(i))
    nama = input("Nama                   : ")
    ipk = float(input("IPK                    : "))
    gaji = int(input("Penghasilan orang tua  : Rp"))
    diproses += 1


    if ipk < 3.00:
        print("Hasil:", nama, "- Tidak memenuhi syarat (IPK < 3,00)")
        tidak_memenuhi += 1
        continue

    if gaji <= 3000000:
        print("Hasil:", nama, "- Beasiswa PENUH")
        penuh += 1
    elif gaji <= 5000000:
        print("Hasil:", nama, "- Beasiswa SEBAGIAN")
        sebagian += 1
    else:
        print("Hasil:", nama, "- Tidak mendapat beasiswa")
        tidak_dapat += 1

    if penuh == 3:
           print("Kuota beasiswa penuh (3 mahasiswa) telah terpenuhi!")
           print("Proses seleksi dihentikan.")
           break

print("===== REKAP SELEKSI =====")
print("Mahasiswa diproses        :", diproses)
print("Beasiswa penuh            :", penuh)
print("Beasiswa sebagian         :", sebagian)
print("Tidak mendapat beasiswa   :", tidak_dapat)
print("Tidak memenuhi syarat IPK :", tidak_memenuhi)
