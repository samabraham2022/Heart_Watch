import socket
from datetime import datetime
import random
import time
from cryptography.fernet import Fernet
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myhmsdb"
)


def collectpid():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT pid FROM patreg")
    pid_list = [row[0] for row in mycursor.fetchall()]
    return pid_list


def encrypt(message, key):
    f = Fernet(key)

    encrypted_message = f.encrypt(message.encode())
    return encrypted_message
device_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device_socket.connect(('localhost', 8888))
while True:
    patient_list = collectpid()
    patientid = random.choice(patient_list)
    value = random.randint(40, 100)
    message = encrypt(str(patientid)+","+str(value)+","+str(datetime.timestamp(
        datetime.now())), 'iVvNNUzoA2fEM_b-02z9W8XvskMXkw_cMMJ51YGTZn0=')
    device_socket.send(message)
    time.sleep(0.3)

# Close the socket connection
device_socket.close()
