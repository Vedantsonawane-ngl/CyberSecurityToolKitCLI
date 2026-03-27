# main.py

from auth import authenticate
from cipher import caesar_cipher
from hash_generator import generate_hash
from password_checker import check_password_strength
from breach_checker import check_breach
from utils.helpers import show_banner

def show_menu():
    print("\nWelcome to Cyber Security Tool Kit !!\n")
    print("password  --> Password Checker")
    print("hash      --> Hash Generator")
    print("cipher    --> Caesar Cipher")
    print("breach    --> Breach Checker")
    print("exit      --> Exit\n")


def main():
    
    show_banner()
    authenticate()

    while True:
        show_menu()
        choice = input("Enter Command: ").lower().strip()

        if choice == "password":
             check_password_strength()

        elif choice == "hash":
            generate_hash()

        elif choice == "cipher":
            caesar_cipher()

        elif choice == "breach":
              check_breach()

        elif choice == "exit":
            print("Exiting...\n")
            break

        else:
            print("Invalid input. Please try again\n")


if __name__ == "__main__":
    main()