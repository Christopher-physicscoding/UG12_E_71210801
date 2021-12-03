z = [ 3, 20, 100, -35, 50 ]
print(z)

def kecil(bilangan):
  minimal = bilangan[0]
  for angka in bilangan:
    if angka < minimal:
        minimal = angka
  return minimal

def besar(deret):
  maksimal = deret[0]
  for number in deret:
    if number > maksimal:
      maksimal = number
  return maksimal

print('Nilai terbesar:', besar(z))
print('Nilai terkecil:',  kecil(z))

print(" ")
print(" ")


k = [ 3, 20, 90, 35, 75 ]
print (k)
print('Nilai terbesar:', besar(k))
print('Nilai terkecil:',  kecil(k))
