def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():  # Check if it's a letter
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result += new_char
        else:
            result += char  # Keep special characters unchanged

    return result

# User Input
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))

# Encrypt
encrypted_message = caesar_cipher(message, shift_value, mode="encrypt")
print(f"Encrypted Message: {encrypted_message}")

# Decrypt
decrypted_message = caesar_cipher(encrypted_message, shift_value, mode="decrypt")
print(f"Decrypted Message: {decrypted_message}")
