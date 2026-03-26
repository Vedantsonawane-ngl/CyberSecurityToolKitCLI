# cipher.py

from utils.helpers import post_action

def caesar_cipher():
    while True:
        print("\n=== Caesar Cipher Tool ===")
        print("1. Encrypt")
        print("2. Decrypt")

        choice = input("Enter choice (1/2): ")

        text = input("Enter text: ")

        try:
            shift = int(input("Enter shift value (number): "))
        except ValueError:
            print("❌ Shift must be a number\n")
            continue

        result = ""

        if choice == "1":  # Encrypt
            for char in text:
                if char.isalpha():
                    base = 65 if char.isupper() else 97
                    result += chr((ord(char) - base + shift) % 26 + base)
                else:
                    result += char

            print("\n🔐 Encrypted Text:", result)

        elif choice == "2":  # Decrypt
            for char in text:
                if char.isalpha():
                    base = 65 if char.isupper() else 97
                    result += chr((ord(char) - base - shift) % 26 + base)
                else:
                    result += char

            print("\n🔓 Decrypted Text:", result)

        else:
            print("❌ Invalid choice\n")
            continue

        print()

        # 🔁 Redo / Menu logic
        action = post_action()

        if action == "menu":
            break