hari = str(input("hi Tutu, Silahkan masukkan hari yang ingin anda telusuri: "))
pelajaran = ["1 Algoritma", "3 Sistem Operasi", "4 PAK", "5 Praktikum INLAN", "2 Matematika Teknik", "4 Bhs Indonesia", "6 PKN", "1 IMK", "3 LogMat", "4 Praktekkom", "2 Sistem Basis Data", "4 Praktikum Sistem Basis Data", "6 INLAN"]

if hari == str('senin'):
    for g in range(0,4):
        print("kelas ke-", pelajaran[g])
elif hari == str('selasa'):
    for o in range(4,7):
        print("kelas ke-", pelajaran[o])
elif hari == str("kamis"):
    for o in range(7,10):
        print("kelas ke-", pelajaran[o])
elif hari == str("jumat"):
    for d in range(10,12):
        print("kelas ke-", pelajaran[d])
elif hari == str("rabu"):
    print("Hari rabu Anda tidak ada kelas")
else:
    print("gagal")
    
    

