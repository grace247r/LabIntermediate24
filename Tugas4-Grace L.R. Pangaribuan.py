import random
kata2_rahasia = [
    "Apel", "Mangga", "Jeruk", "Pisang", "Anggur", 
    "Semangka", "Melon", "Nanas", "Alpukat", "Pepaya", 
    "Jambu", "Rambutan", "Manggis", "Durian", "Sirsak"
]

def ambil_kata():
    if not kata2_rahasia:
        return None
    indexkata = random.randint(0,len(kata2_rahasia)-1)
    tebakan_benar = kata2_rahasia.pop(indexkata).upper()
    return tebakan_benar

skor = 0

def hangman():
    global skor
    kata_rahasia = ambil_kata()
    kata_yangditebak = ["_"] * len(kata_rahasia)
    percobaan = 10
    tebakan_terpakai = []

    print("Tebak - tebakan nama buah yuk!")

    while percobaan > 0:
        print("Percobaan ada:", percobaan)
        print("Kata saat ini:", " ".join(kata_yangditebak))

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

        if tebakan in kata_rahasia:
         print("Yey, kamu berhasil tebak", tebakan)
         for i in range(len(kata_rahasia)):
            if kata_rahasia[i] == tebakan:
                kata_yangditebak[i] = tebakan
        else:
            print("YAH,", tebakan, "tidak ada dalam kata rahasia.")

        if "_" not in kata_yangditebak:
            print("Selamat! Anda telah menebak kata rahasia")
            skor += 1
            return

def main_lagi():
   
    global skor

    while kata2_rahasia:
        hangman()
        
        jawaban = input("Apakah Anda ingin lanjut main lagi?(Ya/Tidak)").lower()
        if jawaban != "ya":
            break
    
    print("Permainan selesai. Skor :", skor)

main_lagi()



