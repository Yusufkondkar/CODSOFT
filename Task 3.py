import random
import string


def generate_password(length, uppercase, lowercase, digits, special_chars):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character set must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the length of the password: "))
        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, uppercase, lowercase, digits, special_chars)

        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
