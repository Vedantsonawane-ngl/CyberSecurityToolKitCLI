# breach_checker.py

import os
from utils.helpers import post_action

def check_breach():
    
    while True:

        print("\n" + "="*45)
        print("🔐 BREACH CHECKER TOOL")
        print("="*45)
        print("This tool checks whether your password exists in")
        print("a common leaked password database.\n")

        try:
            base_dir = os.path.dirname(__file__)
            file_path = os.path.join(base_dir, "common_passwords.txt")

            with open(file_path, "r") as file:
                breached_passwords = file.read().splitlines()

            password = input("To check your password please write your password below. ")

            print("\n Breach Check Result:")

            if password in breached_passwords:
                print("⚠️ This password is COMPROMISED!")
                print("❌ Found in common password database")
                print("🚨 Do NOT use this password\n")
            else:
                print("Your Password is Secured. Your password isn't found in Password Data Breach \n")

        except FileNotFoundError:
            print("❌ common_passwords.txt not found in project folder!\n")
            print("👉 Please create it and add common passwords.\n")
            break

    
        action = post_action()

        if action == "menu":
            break