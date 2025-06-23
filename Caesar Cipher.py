def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

if choice == 'e':
    encrypted_message = encrypt(message, shift)
    print(f"\nEncrypted Message: {encrypted_message}")
elif choice == 'd':
    decrypted_message = decrypt(message, shift)
    print(f"\nDecrypted Message: {decrypted_message}")
else:
    print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
