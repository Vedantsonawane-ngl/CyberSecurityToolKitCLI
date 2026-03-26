# breach_checker.py

from utils.helpers import post_action

def check_breach():
    while True:
        try:
            with open("common_passwords.txt", "r") as file:
                breached_passwords = file.read().splitlines()

            password = input("Enter password to check: ")

            print("\n🔍 Breach Check Result:")

            if password in breached_passwords:
                print("⚠️ This password is COMPROMISED!")
                print("❌ Found in common password database")
                print("🚨 Do NOT use this password\n")
            else:
                print("✅ This password is NOT found in common breaches\n")

        except FileNotFoundError:
            print("❌ common_passwords.txt file not found!\n")
            break

        # 🔁 Redo / Menu logic
        action = post_action()

        if action == "menu":
            break