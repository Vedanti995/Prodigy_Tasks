import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Logic
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - start + offset) % 26 + start)
        else:
            result += char
    return result

# Button Handlers
def encrypt_text():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")
        return
    result = caesar_cipher(text, shift, 'encrypt')
    output_label.config(text="Encrypted: " + result)

def decrypt_text():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")
        return
    result = caesar_cipher(text, shift, 'decrypt')
    output_label.config(text="Decrypted: " + result)

# Tkinter GUI
window = tk.Tk()
window.title("Caesar Cipher Tool")
window.geometry("400x350")
window.resizable(False, False)
window.configure(bg="#f2f2f2")

# Input Text
tk.Label(window, text="Enter Text:", bg="#f2f2f2").pack(pady=5)
entry_text = tk.Text(window, height=5, width=40)
entry_text.pack()

# Shift Value
tk.Label(window, text="Enter Shift Value:", bg="#f2f2f2").pack(pady=5)
entry_shift = tk.Entry(window, width=10)
entry_shift.pack()

# Buttons
tk.Button(window, text="Encrypt", command=encrypt_text, bg="#4CAF50", fg="white", width=15).pack(pady=5)
tk.Button(window, text="Decrypt", command=decrypt_text, bg="#2196F3", fg="white", width=15).pack(pady=5)

# Output
output_label = tk.Label(window, text="", wraplength=300, bg="#f2f2f2", fg="#333")
output_label.pack(pady=15)

window.mainloop()
