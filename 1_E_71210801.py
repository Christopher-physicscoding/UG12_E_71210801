s = ' '
awal = int(input("masukkan awal deret: "))
akhir = int(input("masukkan akhir deret: "))

for i in range (awal, akhir):
    if not i % 5 == 0 and not i % 9 == 0:
        if i % 2 == 0:
            s += str(i) + ' '
print(s)
    
      
