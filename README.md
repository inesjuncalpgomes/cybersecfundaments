# Cybersecurity Fundaments

# The bigger picture

Hello world! For my first project, I used PyCharm, and it’s all about a Python script that executes functions of encryption and decryption of files using Caesar Cipher technique, allowing user’s freedom to choose whether he wants do encrypt or decrypt text, and also includes basic hashing functionalities. 

# Techniques

•	Caesar Cipher Encryption: Encrypts text files by switching characters in a specified number of positions.

•	Caesar Cipher Decryption: Decrypts text files that were encrypted using the Caesar Cipher technique.

•	Hashing: Generates a hash of the file content using SHA-256 for integrity checks.

# Software

•	Python 3.12.

•	PyCharm.

# Installation

Clone my repository to your device using:  
https://github.com/inesjuncalpgomes/cybersecfundaments.git

# Practice

1.	Open my project in PyCharm:
    
o	Open PyCharm and select Open from the File menu.

o	Navigate to the cloned project directory and click on it.

2.	Running the Script:
   
o	Open the script file in PyCharm.

o	Run the script by clicking the green run button or pressing Shift + F10.

3.	Script Options: The script accepts command-line arguments for the different functionalities.
   
# Purpose

Encrypt a File (using an input as a command named “encrypt”)
Copy:
#Get user input
input_text = input("Encrypt & decrypt w/ Caesar Cypher")

def encrypt(text, number_of_switches):
    #Encrypt user input
    encrypted_text = ""
    for character in text:
        encrypted_text = encrypted_text + chr((ord(character) - ord("a") + number_of_switches) % 26 + ord("a"))
    print(encrypted_text)

def decrypt(text, number_of_switches):
    #Encrypt user input
    decrypted_text = ""
    for character in text:
        decrypted_text = decrypted_text + chr((ord(character) - ord("a") - 3) % 26 + ord("a"))
    print(decrypted_text)

def get_user_input():
    input_text = input("Insert your text: ")
    input_switches = int(input("Insert number of switches: "))
    encrypt(input_text, input_switches)

get_user_input()

#encrypt("" , 3)
#decrypt("" , 3)

OR (another option)


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

#Usage
texto = input("Insert your text: ")
shift = int(input("Number of switches: "))
mode = input("Choose encrypt/decrypt: ")

try:
    result = caesar_cipher(texto, shift, mode)
    print(f"Result: {result}")
except ValueError as e:
    print(e)

Hash a File
Copy:
import hashlib


def generate_hash_code(input_text):
    hash_object = hashlib.sha256()
    byte_input = input_text.encode
    hash_object.update(byte_input)
    hash_code = hash_object.hexdigest()
    print("hash_code")
OR
import hashlib
def create_sha256_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()

text = "Text to hash"
hashed_text = create_sha256_hash(text)
print(f"The hash is: {hashed_text}")

# Contributing to evolution

Every contribution will be more than welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

# Credits

Python Docs - https://docs.python.org/3/

PyCharm

My wonderful teacher, R.


    
