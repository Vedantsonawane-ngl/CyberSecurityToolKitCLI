# hash_generator.py

import hashlib
from utils.helpers import post_action

def generate_hash():
    while True:

        print("\n" + "="*45)
        print("🔐 HASH GENERATOR TOOL")
        print("="*45)
        print("This tool converts your input text into a secure hash")
        print("using MD5 or SHA-256 algorithms.\n")

        text = input("Enter text to hash: ")

        print("\nChoose your Hash Algorithm for further Procedure:")
        print("1. MD5")
        print("2. SHA-256")

        choice = input("Enter choice (1/2): ")

        if choice == "1":
            hash_result = hashlib.md5(text.encode()).hexdigest()
            print("🔐 MD5 Hash:", hash_result)

        elif choice == "2":
            hash_result = hashlib.sha256(text.encode()).hexdigest()
            print("🔐 SHA-256 Hash:", hash_result)

        else:
            print("Invalid choice. Please try again.\n")
            continue  

        print()

        action = post_action()

        if action == "menu":
            break