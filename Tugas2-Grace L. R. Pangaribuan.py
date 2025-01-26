kata_rahasia = "DBT"
kata_yangditebak = ["_"] * len(kata_rahasia)
percobaan = 6
tebakan_terpakai = []
print("HANGMAN GAME 2!")
while percobaan > 0:
    print("Kata saat ini:", " ".join(kata_yangditebak))
    tebakan = input("Tebak huruf yang menjadi kata rahasia: ").upper()
    if len(tebakan) != 1 or not tebakan.isalpha():
        if tebakan in tebakan_terpakai:
            print("Anda sudah memasukkan ini sebelumnya.")
        else:
            tebakan_terpakai.append(tebakan)
            percobaan -= 1
            print("Salah. Masukkan satu huruf saja.")
            print("Percobaan anda tinggal:", percobaan)
        continue
    if tebakan in tebakan_terpakai:
        print("Anda sudah menebak huruf ini sebelumnya. Coba huruf lain.")
        continue
    tebakan_terpakai.append(tebakan)
    if tebakan in kata_rahasia:
        print("Tebakan Anda benar!")
        for i in range(len(kata_rahasia)):
            if kata_rahasia[i] == tebakan:
                kata_yangditebak[i] = tebakan
                percobaan -= 1
    else:
        print("Yah, tebakan kamu salah.")
        percobaan -= 1
        print("Percobaan anda tinggal:", percobaan)
    if "_" not in kata_yangditebak:
        print("Selamat! Anda telah menebak kata rahasia:", kata_rahasia)
        break
if "_" in kata_yangditebak:
    print("Sayang sekali, kamu kehabisan percobaan.")
