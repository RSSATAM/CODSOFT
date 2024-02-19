import random
import string

def generate_password(length):
    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Shuffle the characters to make the password more random
    shuffled_characters = random.sample(all_characters, len(all_characters))

    # Generate password using shuffled characters
    password = ''.join(random.choice(shuffled_characters) for _ in range(length))

    return password

def main():
    print("Password Generator App")
    print("-----------------------")

    # Prompt user for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    # Generate password
    password = generate_password(length)
    
    # Display generated password
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()

