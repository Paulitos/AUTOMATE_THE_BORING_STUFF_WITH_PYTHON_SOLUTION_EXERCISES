# Strong Password Detection Page 186 Chapter 7
import re

def is_strong_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # If all checks pass, the password is strong
    return True

# Test the function
password1 = "Passw0rd"  # Strong password
password2 = "weakpass"  # Missing uppercase and digit
password3 = "Short1"    # Short length
password4 = "AllLowercase"  # Missing uppercase and digit

print(is_strong_password(password1))  # True
print(is_strong_password(password2))  # False
print(is_strong_password(password3))  # False
print(is_strong_password(password4))  # False

