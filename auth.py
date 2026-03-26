# This is authentication -- auth.py

def authenticate():
    correct_password="vedantharish123"

    while True:
        user_input=input("Please enter your alloted Password: ")

        if user_input==correct_password:
            print("Access Granted !\n ")
            break

        else:
            print("Password is incorrect. Try again.\n")