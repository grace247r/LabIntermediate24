kata_rahasia = "prasetiya"
kata_yangditebak = ["_"]* len(kata_rahasia) 
print("MAIN TEBAK KATA YUK!") 
while "_" in kata_yangditebak:
    print("Kata saat ini :"," ".join(kata_yangditebak))
    tebakan = input("Tebak huruf yang menjadi kata rahasia: ").lower()
    if len(tebakan) != 1 or not tebakan.isalpha():
        print("Salah. Masukkan satu huruf saja.")
        continue
    if tebakan in kata_yangditebak:
        print("Anda sudah memasukkan huruf ini, silakan input huruf")
    if tebakan in kata_rahasia:
        print("Tebakan Anda benar!")
        for i in range(len(kata_rahasia)):
            if kata_rahasia[i] == tebakan:
                kata_yangditebak[i] = tebakan
    else:
        print("Yah, tebakan kamu salah.")
    if "_" not in kata_yangditebak:
        print("Selamat! Anda telah menebak kata rahasia:", kata_rahasia)
        break