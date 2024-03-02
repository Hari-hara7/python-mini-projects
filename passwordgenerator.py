import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    # Define character sets based on criteria
    letters = string.ascii_letters if uppercase or lowercase else ''
    digits = string.digits if numbers else ''
    punctuation = string.punctuation if special_chars else ''

    # Combine character sets based on criteria
    all_chars = letters + digits + punctuation

    # Ensure at least one character set is selected
    if not all_chars:
        print("Error: At least one of uppercase, lowercase, numbers, or special characters should be selected.")
        return None

    # Generate random password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# Example: Generate a password with length 16 including uppercase, lowercase, numbers, and special characters
password = generate_password(length=16, uppercase=True, lowercase=True, numbers=True, special_chars=True)
print("Generated Password:", password)
