# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            # Preserve the case of the character
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just encryption with negative shift

# Main program to allow user input
def caesar_cipher():
    print("Caesar Cipher Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose 'E' for encryption or 'D' for decryption.")
        return
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    else:
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")

# Run the program
if __name__ == "__main__":
    caesar_cipher()
