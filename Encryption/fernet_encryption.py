from cryptography.fernet import Fernet

message = "Wakko Warner say's Wahhoooo!"

key = b'iceDucHrs_no69A7yl6tNDgRGC7mXEr7pAvmPMlixiI='
# key = Fernet.generate_key()
print(f'Key: {key}')

fernet = Fernet(key)
encrypted_message = fernet.encrypt(message.encode())

print(f'Original Message: {message}')
print(f'Encrypted Message: {encrypted_message}')

decrypted_message = fernet.decrypt(encrypted_message).decode()
print(f'Decrypted Message: {decrypted_message}')