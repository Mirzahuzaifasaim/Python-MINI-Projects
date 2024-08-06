import json
import os
from cryptography.fernet import Fernet

# Function to generate and save a new key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Function to save passwords to a JSON file
def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Function to load passwords from a JSON file
def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            return json.load(file)
    return {}

# Main function to manage the password manager
def main():
    # Generate a key if it doesn't exist
    if not os.path.exists("key.key"):
        generate_key()

    key = load_key()
    passwords = load_passwords()

    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            encrypted_password = encrypt_message(password, key)
            passwords[service] = encrypted_password.decode()
            save_passwords(passwords)
            print(f"Password for {service} added successfully!")

        elif choice == '2':
            service = input("Enter the service name: ")
            if service in passwords:
                encrypted_password = passwords[service].encode()
                decrypted_password = decrypt_message(encrypted_password, key)
                print(f"Password for {service} is: {decrypted_password}")
            else:
                print(f"No password found for {service}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
