import argon2

password = b'Pinky and The Brain'
hashed_password = argon2.hash_password(password)

print(hashed_password)