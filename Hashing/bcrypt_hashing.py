import bcrypt

password = b"Pinky and The Brain"

salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

print(f'Salt: {salt}')
print(f'Plaintext: {password}')
print(f'Hashed Password: {hashed_password}')

print({
      "name": "Johnathan",
      "date_joined": "2024-06-01",
      "password": f"{hashed_password}"
})

user_entry = b"password"
if(bcrypt.hashpw(user_entry, salt) == hashed_password):
    print("Password Correct")
else:
    print("Password Incorrect")