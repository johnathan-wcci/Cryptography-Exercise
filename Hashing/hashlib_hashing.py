import hashlib

password = "Pinky and The Brain"
salt = "ThisIsASalt"

database_password = password+salt
print(f"database password: {database_password}")

hashed_password = hashlib.md5(database_password.encode())
print(f"hashed password: {hashed_password.hexdigest()}")