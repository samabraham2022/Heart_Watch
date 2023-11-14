import socket
from datetime import datetime
import random
import time
from cryptography.fernet import Fernet
import mysql.connector
from keras.models import load_model
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objs as go
import plotly.express as px
from scipy.signal import medfilt, butter, filtfilt
import pywt
from sklearn.model_selection import train_test_split
import scipy.signal
from keras.models import Sequential
from keras.layers import LSTM, Dense, Reshape
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import roc_auc_score
model = load_model('model.h5')
from prediction import featureselection,format_data,model_predict
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="samgeorge",
    database="myhmsdb"
)


def collectpid(table):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT pid FROM "+table)
    pid_list = [row[0] for row in mycursor.fetchall()]
    return pid_list
def delete_records(l):
    mycursor = mydb.cursor()
    for i in l:
        sql_delete = f"DELETE FROM ecg WHERE pid = {i}"
        mycursor.execute(sql_delete)
    mydb.commit()
def add_patients_to_ecg(l):
    mycursor = mydb.cursor()
    for pid in l:
        try:
            mycursor.execute("INSERT INTO ecg values ("+str(pid)+",'')")
        except:
            pass
    mydb.commit()
def predict(pid,values):
    mycursor = mydb.cursor()
    output = model_predict([values])
    if output:
        sql = "UPDATE patreg SET Heart_Attack = '"+str(True)+"' WHERE pid = '"+str(pid)+"'"
        mycursor.execute(sql)
        mydb.commit()
    else:
        sql = "UPDATE patreg SET Heart_Attack = '"+str(False)+"' WHERE pid = '"+str(pid)+"'"
        mycursor.execute(sql)
        mydb.commit()


def datagen():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ecg")
    records = mycursor.fetchall()
    for i in records:
        ecg_each_user = [float(j) for j in i[1].split(" ")]
        pid = i[0]
        if len(ecg_each_user) == 140:
            predict(pid,ecg_each_user)
    

patient_list = collectpid("patreg")
patient_list_ecg = collectpid("ecg")
rest = [x for x in patient_list_ecg if x not in patient_list]
delete_records(rest)
add_patients_to_ecg(patient_list)
while(1):
    datagen()



