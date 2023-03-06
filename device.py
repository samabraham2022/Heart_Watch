import socket
from datetime import datetime
import random
import time
from cryptography.fernet import Fernet
def encrypt(message, key):
    f = Fernet(key)

    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

device_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device_socket.connect(('localhost', 8888))
patientid = 1234

while True:
    value = random.randint(40,100)
    message = encrypt(str(patientid)+","+str(value)+","+str(datetime.timestamp(datetime.now())),'iVvNNUzoA2fEM_b-02z9W8XvskMXkw_cMMJ51YGTZn0=')
    device_socket.send(message)
    time.sleep(1)

# Close the socket connection
device_socket.close()
