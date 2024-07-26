# Get user input
input_text = input("Encrypt & decrypt w/ Caesar Cypher")

def encrypt(text, number_of_switches):
    # Encrypt user input
    encrypted_text = ""
    for character in text:
        encrypted_text = encrypted_text + chr((ord(character) - ord("a") + number_of_switches) % 26 + ord("a"))
    print(encrypted_text)

def decrypt(text, number_of_switches):
    # Encrypt user input
    decrypted_text = ""
    for character in text:
        decrypted_text = decrypted_text + chr((ord(character) - ord("a") - 3) % 26 + ord("a"))
    print(decrypted_text)

def get_user_input():
    input_text = input("Insert your text: ")
    input_switches = int(input("Insert number of switches: "))
    encrypt(input_text, input_switches)

get_user_input()

#encrypt("estetoscopio" , 6)
#decrypt("hvwhwrvfrslr , 6")


