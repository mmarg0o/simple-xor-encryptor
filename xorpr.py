
from pystyle import Colorate, Colors, Write, Center
import time
from pyfiglet import * 

KEY = 0X42 # XOR KEY

INPUT_FILE = "example.txt"
ENCRYPTED_FILE = "encrypted.bin"
DECRYPTED_FILE = "decrypted.txt"

def display_banner():
    banner = r"""
__   _____________   _____ _____  _____ _     
\ \ / /  _  | ___ \ |_   _|  _  ||  _  | |    
 \ V /| | | | |_/ /   | | | | | || | | | |    
 /   \| | | |    /    | | | | | || | | | |    
/ /^\ \ \_/ / |\ \    | | \ \_/ /\ \_/ / |____
\/   \/\___/\_| \_|   \_/  \___/  \___/\_____/
"""
    print(Colorate.Horizontal(Colors.white_to_blue, banner))


def xor_data(data: bytes, key: int) -> bytes:
    return bytes(b ^ key for b in data)

def encrypted_file():
    try:
        with open(INPUT_FILE, "rb") as f:
         data = f.read()
    except FileNotFoundError:
        print("File not found")
        return

    encrypted = xor_data(data, KEY)

    with open("encrypted.bin", "wb") as f:
        f.write(encrypted)

    with open(ENCRYPTED_FILE, "wb") as f:
        f.write(encrypted)

        Write.Print("\n File encrypted -> encrypted.bin", Colors.gray, interval = 0.07)

def decrypted_file():
    with open(ENCRYPTED_FILE, "rb") as f:
        data = f.read()

        decrypted = xor_data(data,  KEY)

    with open(DECRYPTED_FILE, "wb") as f:
        f.write(decrypted)

    Write.Print("\n File decrypted -> decrypted.txt ", Colors.gray, interval= 0.07)
    print(decrypted.decode(errors="ignore"))

def view_file():
    with open(INPUT_FILE, 'r', encoding="utf-8") as f:
        Write.Print("\n File contence: ", Colors.gray, interval = 0.07)
        print(f.read())


def menu():
    print()
    print(Colorate.Color(Colors.gray, "[1] Encrypt file"))
    print(Colorate.Color(Colors.gray, "[2] Decrypt file"))
    print(Colorate.Color(Colors.gray, "[3] View original file"))
    print(Colorate.Color(Colors.red, "[0] Exit"))
    print()

    return input(">>> ")
    

def main():
    
     
    while True:
        display_banner()
        choice = menu()

        if choice == "1":
            encrypted_file()
        elif choice == "2":
            decrypted_file()
        elif choice == "3":
            view_file()
        elif choice == "0":
            break
        else:
            print(Colorate.Color(Colors.red, "Wrong input"))
        
        time.sleep(1)
     

if __name__ == "__main__":
    main()