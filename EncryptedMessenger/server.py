import socket
from cryptography.fernet import Fernet

# Initialize Cipher
key = b'iceDucHrs_no69A7yl6tNDgRGC7mXEr7pAvmPMlixiI=' # Remember PlainText Keys are bad
fernet = Fernet(key)

# Initialize Server
serverSocket = socket.socket()
serverSocket.bind(("127.0.0.1", 8080))
serverSocket.listen()

while(True):
    (clientConnection, clientAddress) = serverSocket.accept()
    message = fernet.decrypt(clientConnection.recv(1024))
    print(f"Received from {clientAddress}: {message.decode()}")