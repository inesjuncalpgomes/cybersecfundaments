def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "encrypt":
        shift_amount = shift
    elif mode == "decrypt":
        shift_amount = -shift
    else:
        raise ValueError("Mode must be 'encrypt' or 'decrypt'")

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char

    return result

#How to use
texto = input("Insert your text: ")
shift = int(input("Number of switches: "))
mode = input("Choose encrypt/decrypt: ")

try:
    result = caesar_cipher(texto, shift, mode)
    print(f"Result: {result}")
except ValueError as e:
    print(e)
