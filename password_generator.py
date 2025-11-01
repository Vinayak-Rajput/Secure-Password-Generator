import secrets
import string
import random

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    """
    Generates a secure, cryptographically strong password.
    """
    
    # Define character sets
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all allowed characters into one pool
    all_characters = ""
    if use_lowercase:
        all_characters += letters_lower
    if use_uppercase:
        all_characters += letters_upper
    if use_digits:
        all_characters += digits
    if use_special_chars:
        all_characters += special_chars

    # This list will hold the password characters
    password_chars = []
    
    # 1. Guarantee at least one of each required character type
    if use_lowercase:
        password_chars.append(secrets.choice(letters_lower))
    if use_uppercase:
        password_chars.append(secrets.choice(letters_upper))
    if use_digits:
        password_chars.append(secrets.choice(digits))
    if use_special_chars:
        password_chars.append(secrets.choice(special_chars))

    # 2. Fill the remaining length with characters from the total pool
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(all_characters))

    # 3. Shuffle the list to mix up the guaranteed characters
    random.shuffle(password_chars)

    # 4. Join the list into a final string
    return "".join(password_chars)

def get_user_preferences():
    """
    Gets password length and character type preferences from the user.
    Includes input validation.
    """
    
    # Get user input for password length with validation
    while True:
        try:
            length = int(input("Enter the desired password length (min 8): "))
            if length < 8:
                print("Error: Password length must be at least 8 characters.")
            else:
                break # Exit loop if length is valid
        except ValueError:
            print("Error: Please enter a valid number.")

    # Get user preferences for character types
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Edge case: Check if at least one character type is selected
    if not (use_lowercase or use_uppercase or use_digits or use_special_chars):
        print("\nError: You must select at least one character type. Please try again.\n")
        return get_user_preferences() # Recursively call to start over

    return length, use_lowercase, use_uppercase, use_digits, use_special_chars

def main():
    """
    Main function to run the password generator.
    """
    print("--- Secure Password Generator ---")

    # Get user preferences
    length, use_lowercase, use_uppercase, use_digits, use_special_chars = get_user_preferences()

    # Generate and display password
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
