import socket
from datetime import datetime
import time
from cryptography.fernet import Fernet
import mysql.connector
import requests
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="samgeorge",
  database="myhmsdb"
)
def blockchain():
    data = requests.get('http://127.0.0.1:5000/mine_block')
    print(data.text)
def decrypt(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()
def updater(pid,rate):
    mycursor = mydb.cursor()
    sql = "UPDATE patreg SET Heart_Rate = '"+str(rate)+"' WHERE pid = '"+str(pid)+"'"
    mycursor.execute(sql)
    mydb.commit()
def ecg_updater(pid,ecg):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ecg FROM ecg WHERE pid = "+str(pid))
    queryresult = mycursor.fetchone()[0].strip().split(" ")
    result = []
    if len(queryresult) == 0:
        result.append(ecg)
    elif len(queryresult)<140:
        result = queryresult
        result.append(ecg)
    else:
        result = queryresult
        result.pop(0)
        result.append(ecg)
    output = " ".join(result)
    sql = "UPDATE ecg SET ecg = '"+output+"' WHERE pid = '"+str(pid)+"'"
    mycursor.execute(sql)
    mydb.commit()
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_socket.bind(('localhost', 8888))
receiver_socket.listen(1)
print("Waiting for device to connect...")
device_socket, device_address = receiver_socket.accept()
print("Device connected:", device_address)
while True:
    message = device_socket.recv(1024)
    values = decrypt(message.decode(),'iVvNNUzoA2fEM_b-02z9W8XvskMXkw_cMMJ51YGTZn0=').split(',')
    pid = values[0]
    heartrate = values[1]
    ecg = values[2]
    updater(pid,heartrate)
    ecg_updater(pid,ecg)
    #blockchain()
    time.sleep(0.1)
    dt = datetime.now()
    ts = datetime.timestamp(dt)


device_socket.close()
receiver_socket.close()
