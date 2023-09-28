# password_checker.py

def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

# Get user input for the password to check
password = input("Enter a password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is too short. It must be at least 8 characters long.")
