import hashlib


def generate_hash_code(input_text):
    hash_object = hashlib.sha256()
    byte_input = input_text.encode
    hash_object.update(byte_input)
    hash_code = hash_object.hexdigest()
    print("hash_code")

