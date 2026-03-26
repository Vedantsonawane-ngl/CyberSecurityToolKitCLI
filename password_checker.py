# password_checker.py

import re
from utils.helpers import post_action

def check_password_strength():
    while True:
        password = input("Enter password to check: ")

        score = 0
        feedback = []

        # Length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Use at least 8 characters")

        # Uppercase
        if re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback.append("Add uppercase letters")

        # Lowercase
        if re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("Add lowercase letters")

        # Digit
        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("Add numbers")

        # Special character
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            feedback.append("Add special characters")

        # Result
        print("\n🔐 Password Analysis:")

        if score == 5:
            print("✅ Very Strong Password 💪")
        elif score >= 3:
            print("⚠️ Medium Password")
        else:
            print("❌ Weak Password")

        print(f"Score: {score}/5")

        # Suggestions
        if feedback:
            print("\nSuggestions:")
            for tip in feedback:
                print(f"- {tip}")

        print()

        # 🔁 Redo / Menu logic
        action = post_action()

        if action == "menu":
            break