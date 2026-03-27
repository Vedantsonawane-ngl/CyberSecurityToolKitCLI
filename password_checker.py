# password_checker.py

import re
from utils.helpers import post_action

def check_password_strength():
    while True:

        print("\n" + "="*45)
        print("🔐 PASSWORD CHECKER TOOL")
        print("="*45)
        print("This tool analyzes your password strength based on")
        print("security rules like length, case, numbers, and symbols.\n")

        password = input("Enter password to check: ")

        score = 0
        feedback = []

        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Use at least 8 characters")

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback.append("Add uppercase letters")

        if re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("Add lowercase letters")

        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("Add numbers")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            feedback.append("Add special characters")

        
        print("\n Password Analysis:")

        if score == 5:
            print("✅ Very Strong Password ")
        elif score >= 3:
            print("⚠️ Medium Password, Need some changes.")
        else:
            print("Weak Password. Please go for a Strong and Unique Password.")

        print(f"Score: {score}/5")

        if feedback:
            print("\nSuggestions:")
            for tip in feedback:
                print(f"- {tip}")

        print()

        action = post_action()

        if action == "menu":
            break