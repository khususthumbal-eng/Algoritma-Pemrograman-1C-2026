# # Menara Lampu Hias
# while True:
#     n = int(input("Masukkan tinggi setengah menara (2-15): "))
#     if n >= 2 and n <= 15:
#         break
#     print("Input tidak valid, silakan ulangi!")

# baris = list(range(1, n + 1)) + list(range(n - 1, 0, -1))

# for i in baris:
#     teks = ""
#     # angka naik dari 1 sampai i
#     for k in range(1, i + 1):
#         teks += str(k % 10)
#     # angka turun dari i-1 sampai 1
#     for k in range(i - 1, 0, -1):
#         teks += str(k % 10)
#     # rata tengah
#     print(" " * (n - i) + teks)
n = int(input())
data = list(map(int, input().split()))

# 1. Total porsi
total = 0
for x in data:
    total += x

# 2. Rata-rata
rata = total / n

# 3. Hari tertinggi (yang paling awal jika ada yang sama)
tertinggi = data[0]
hari = 1
for i in range(1, n):
    if data[i] > tertinggi:   # pakai ">" agar hari paling awal tetap terpilih
        tertinggi = data[i]
        hari = i + 1

# 4. Jumlah hari di atas rata-rata
di_atas = 0
for x in data:
    if x > rata:
        di_atas += 1

# 5. Kenaikan beruntun terpanjang
terpanjang = 1
saat_ini = 1
for i in range(1, n):
    if data[i] > data[i - 1]:
        saat_ini += 1
    else:
        saat_ini = 1
    if saat_ini > terpanjang:
        terpanjang = saat_ini

print(f"Total: {total}")
print(f"Rata-rata: {rata:.2f}")
print(f"Tertinggi: hari ke-{hari} ({tertinggi} porsi)")
print(f"Di atas rata-rata: {di_atas} hari")
print(f"Kenaikan terpanjang: {terpanjang} hari")