import main

def start():
    while True:
        print('Ini Warung Apps')
        play_again = input('Kembali ke Menu Utama? [y/n]')
        
        if play_again == "y":
            main.menu()

if __name__ == '__main__':
    start()