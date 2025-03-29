def check_password_strength(password):
    strength = 0
    strength_levels = ["Weak", "Moderate", "Strong", "Very Strong"]

    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/`~" for char in password):
        strength += 1

    # Prevent out-of-range index error
    strength = min(strength, len(strength_levels) - 1)

    print(f"Password Strength: {strength_levels[strength]}")

password = input("Enter a password to check its strength: ")
check_password_strength(password)
