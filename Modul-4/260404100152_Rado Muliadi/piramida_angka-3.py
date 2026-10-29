
n = int(input("Masukkan bilangan bulat positif n: "))
for i in range(1, n + 1):
    for R in range(1, i + 1):
        print(R, end="")
        
    for s in range(2 * (n - i) + 2):
        print(" ", end="")
        
    for R in range(i, 0, -1):
        print(R, end="")
    print()
