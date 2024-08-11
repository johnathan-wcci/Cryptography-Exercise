import rsa

pub, private = rsa.newkeys(1024)
print(pub)
print(private)

message = "The same thing we do every night, Pinky…Try and take over the world!"

encrypted_message = rsa.encrypt(message.encode(), pub)

print(f'Original Message: {message}')
print(f'Encrypted Message: {encrypted_message}')

decrypted_message = rsa.decrypt(encrypted_message, private).decode()

print(f'Decrypted Message: {decrypted_message}')
