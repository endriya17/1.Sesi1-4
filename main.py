from libs import welcome_message, exit_program
from games import cupy
from tools import warung

def menu():
    user_option= int(input(f'Menu Program:\n1. Games Cupy\n2. Warung Mini\n3. Keluar Program\n\nSilahkan Pilih: '))
    return  user_option

    if user_option == 1:
        cupy.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit.program()
    else:
        print('Hanya Boleh Pilih yang tersedia di menu!')

def main():
    welcome_message() #Tampilkan Judul Awal 
    menu()   
      
if __name__ == '__main__':
    main()
