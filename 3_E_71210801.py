angka = int(input("masukkan angka: "))
rumus = 2 * angka - 2

for i in range (0, angka):
    for a in range (0,rumus):
        print ( end = " ")
    rumus = rumus - 1
    for b in range (0, i ):
        print("*", end = " ")
    print()
    
rumus2 = angka - 2
for i in range (angka, -1, -1):
    for c in range (rumus2,0,-1):
        print (end = " ")
    rumus2 = rumus2 + 1
    for d in range (0, i ):
        print("*", end = " ")
    print()
