import random
import string

def generate_password(length=12, include_symbols=True, include_uppercase=True, include_lowercase=True, include_numbers=True):
    """Generates a strong random password with customizable options.

    Args:
        length (int): The desired length of the password.
        include_symbols (bool): Whether to include symbols in the password.
        include_uppercase (bool): Whether to include uppercase letters in the password.
        include_lowercase (bool): Whether to include lowercase letters in the password.
        include_numbers (bool): Whether to include numbers in the password.

    Returns:
        str: The generated password.
    """

    characters = ""
    if include_symbols:
        characters += string.punctuation
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'

    try:
        password = generate_password(password_length, include_symbols, include_uppercase, include_lowercase, include_numbers)
        print("Generated password:", password)
    except ValueError:
        print("Error: At least one character type must be selected.")
