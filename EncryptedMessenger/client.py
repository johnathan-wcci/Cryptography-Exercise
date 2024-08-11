import socket
from cryptography.fernet import Fernet

# Initialize Cipher
key = b'iceDucHrs_no69A7yl6tNDgRGC7mXEr7pAvmPMlixiI=' # Remember PlainText Keys are bad
fernet = Fernet(key)

# Connect To Server
server = ("127.0.0.1", 8080)
serverSocket = socket.socket()
serverSocket.connect(server)

message = ""
while (message != "quit"):
    message = input(f'Send Message To {server[0]}:{server[1]}: ')
    print(f'Message Sent to {server[0]}:{server[1]}!')
    serverSocket.send(fernet.encrypt(message.encode()))

