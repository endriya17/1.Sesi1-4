import random
import emoji
import main

def start():
    #print emoji ucapan kalah menah
    notif_winner = "Selamat" + (emoji.emojize(":trophy:")*8)
    notif_loose = "Maaf" + (emoji.emojize(":thumbs_down:") *8)
    nama_user = input("Masukan Nama Anda: ")

    while nama_user == "":
        nama_user = input("isi dulu nama anda: ")
        
    while True:
        cupy_position = random.randint (1, 4)
        
        bentuk_goa = "|__|"
        goa_kosong = [bentuk_goa] * 4 # Ini Tetep Harus Kosong
        
        goa = goa_kosong.copy() # Ini Adalah Tempat Baru  untuk Cupy
        goa[cupy_position -1] = "|0_0|"
        
        goa_kosong = '  '.join(goa_kosong)
        goa = '  '.join(goa)
        
        print(f"\nHalo {nama_user}! Coba perhatikan goa dibawah ini")
        print(f"Cari Cupy dimana {goa_kosong}?")
        
        pilihan_user = (input("Menurut kamu di goa nomor berapa Cupy Berada? [1 / 2 / 3 / 4]: "))

        # while pilihan_user == "":
        #     pilihan_user = input("Jangan dikosongin Bos, Pilih angka (1-4):")

        while pilihan_user == "" or not pilihan_user.isdigit():
            pilihan_user = (input("Salah Bos Masukan angka 1 - 4: "))
            
        konfirmasi_pilihan = input("Apakah anda yakin dengan pilihan anda [y/n]:")
            
        if konfirmasi_pilihan == "n":
            print("Program dihentikan")
            exit()
            
        elif konfirmasi_pilihan == "y":
            if int(pilihan_user) == cupy_position:
                print(f"\nJawaban Kamu adalah {pilihan_user}")
                print(f"\nSelamat {nama_user} \nkamu menang posisi Cupy ada di goa nomor {cupy_position} dan pilihan kamu adalah {pilihan_user} \n{goa}")
                
                print(notif_winner)
            else:
                print(f"\nKamu kalah \nCupy tidak ada disitu tapi ada di goa nomor {cupy_position} \nSedangankan kamu memilih goa nomor {pilihan_user} \n{goa}")
                
                print(notif_loose)
        else:
            print("Silahkan ulangi programnya!")
            exit()
            
        play_again = input ("\nApakah mau udahan atau lanjut lagi? [y/n]")
        if play_again == "n":
            main.menu()
            break
        
        elif play_again == "y":
            continue
        
        else:
            print("Masukan Salah Silahkan Ulangi Progam!")
            break
        
    print("Program Selesai!")
    
if __name__ == '__main__':
    start()