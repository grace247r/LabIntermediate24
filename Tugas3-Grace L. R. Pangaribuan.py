def tampilkan_kata(kata_yangditebak):
    print("Kata saat ini:", " ".join(kata_yangditebak))

def perbarui_kata(tebakan, kata_rahasia, kata_yangditebak):
    if tebakan in kata_rahasia:
        print("Yey, kamu berhasil tebak", tebakan)
        for i in range(len(kata_rahasia)):
            if kata_rahasia[i] == tebakan:
                kata_yangditebak[i] = tebakan
        return True 

def hangman3():
    kata_rahasia = "DBT"
    kata_yangditebak = ["_"] * len(kata_rahasia)
    percobaan = 6
    tebakan_terpakai = []

    print("HANGMAN GAME 2!")

    while percobaan > 0:
        print("\nPercobaan ada:", percobaan)
        tampilkan_kata(kata_yangditebak)

        tebakan = input("Tebak huruf yang menjadi kata rahasia: ").upper()

        if len(tebakan) != 1 or not tebakan.isalpha():
            if tebakan in tebakan_terpakai:
                print("Anda sudah memasukkan ini sebelumnya.")
            else:
                print("Salah. Masukkan SATU HURUF saja.")
                percobaan -= 1 
                tebakan_terpakai.append(tebakan)
            continue

        if tebakan in tebakan_terpakai:
            print("Anda sudah menebak ini sebelumnya. Coba huruf lain.")
            continue  

        tebakan_terpakai.append(tebakan) 
        percobaan -= 1 

        if not perbarui_kata(tebakan, kata_rahasia, kata_yangditebak):
            print("YAH,", tebakan, "tidak ada dalam kata rahasia.")

        if "_" not in kata_yangditebak:
            print("Selamat! Anda telah menebak kata rahasia")
            return

    print("Sayang sekali, kamu kehabisan percobaan.")

hangman3()
