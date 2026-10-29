total_gaji = 0

for hari in range(1, 8):
    print("Hari ke-" + str(hari))
    while True:
        lembur = int(input("Jam lembur : "))
        if lembur >= 0 and lembur != 5 and lembur != 7:
            break
        print("Jam lembur tidak sesuai ketentuan, cobalah ulangi input!")

    if lembur > 8:
        print("Jumlah lembur melebihi batas yang ditentukan, upah lembur tidak dihitung")
        upah_lembur = 0
    elif lembur == 8:
        upah_lembur = 300000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 4:
         upah_lembur = 100000
    else:
        upah_lembur = lembur * 25000

    while True:
        shift = input("Shift malam (y/t) : ")
        if shift == "y" or shift == "t":
            break
        print("Masukan tidak valid, ketik y atau t!")

    if shift == "y":
        tambahan = 50000
    else:
        tambahan = 0

    gaji_hari = 100000 + upah_lembur + tambahan
    print("Gaji hari ke-" + str(hari) + " : Rp", gaji_hari)
    total_gaji += gaji_hari

print("Total gaji mingguan : Rp", total_gaji)
