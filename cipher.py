from utils.helpers import post_action

def caesar_cipher():
    while True:
        print("\n" + "="*45)
        print("🔐 CIPHER TOOL (Caesar Cipher)")
        print("="*45)
        print("This tool allows you to encrypt or decrypt text")
        print("using a shift-based substitution technique.\n")

        print("1. Encrypt")
        print("2. Decrypt")

        choice = input("Enter choice (1/2): ")

        text = input("Enter text: ")

        try:
            shift = int(input("Enter shift value (number): "))
        except ValueError:
            print(" Shift must be a number\n")
            continue

        result = ""

        if choice == "1": 
            for char in text:
                if char.isalpha():
                    base = 65 if char.isupper() else 97
                    result += chr((ord(char) - base + shift) % 26 + base)
                else:
                    result += char

            print("\nYour Encrypted Text:", result)

        elif choice == "2": 
            for char in text:
                if char.isalpha():
                    base = 65 if char.isupper() else 97
                    result += chr((ord(char) - base - shift) % 26 + base)
                else:
                    result += char

            print("\nYour Decrypted Text:", result)

        else:
            print("Invalid choice. Please try again...\n")
            continue

        print()

        action = post_action()

        if action == "menu":
            break