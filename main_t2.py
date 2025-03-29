from PIL import Image
import numpy as np

def encrypt_image(image_path, key, encrypted_path):
    """Encrypt an image by applying an XOR operation on pixel values."""
    img = Image.open(image_path).convert("RGB")  # Open and convert image to RGB
    pixels = np.array(img, dtype=np.uint8)  # Convert image to NumPy array

    # Apply XOR encryption with the key
    encrypted_pixels = pixels ^ np.uint8(key)

    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_pixels)
    encrypted_img.save(encrypted_path)
    print(f"🔒 Encrypted image saved as: {encrypted_path}")

def decrypt_image(encrypted_path, key, decrypted_path):
    """Decrypt an image by applying XOR again (XOR is reversible)."""
    encrypt_image(encrypted_path, key, decrypted_path)  # XOR again to decrypt
    print(f"🔓 Decrypted image saved as: {decrypted_path}")

# Example Usage
image_path = "input.jpg"   # Replace with your actual image path
encrypted_path = "encrypted.jpg"
decrypted_path = "decrypted.jpg"
key = 42  # Secret key (must be the same for encryption & decryption)

encrypt_image(image_path, key, encrypted_path)   # Encrypt the image
decrypt_image(encrypted_path, key, decrypted_path)  # Decrypt it back
