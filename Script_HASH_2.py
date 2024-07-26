import hashlib
def create_sha256_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()

text = "Text to hash"
hashed_text = create_sha256_hash(text)
print(f"The hash is: {hashed_text}")



