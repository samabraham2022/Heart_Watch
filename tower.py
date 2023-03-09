import socket
from datetime import datetime
import time
from cryptography.fernet import Fernet
def decrypt(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_socket.bind(('localhost', 8888))
receiver_socket.listen(1)
print("Waiting for device to connect...")
device_socket, device_address = receiver_socket.accept()
print("Device connected:", device_address)
while True:
    message = device_socket.recv(1024)
    values = decrypt(message.decode(),'iVvNNUzoA2fEM_b-02z9W8XvskMXkw_cMMJ51YGTZn0=').split(',')
    print("Received values from device:", values)
    time.sleep(1)
    dt = datetime.now()
    ts = datetime.timestamp(dt)

    print(ts)
device_socket.close()
receiver_socket.close()
