import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal, misc 
from scipy.fftpack import fft, ifft, fftfreq
import socket
import struct #pack in double to send over network
import time
print("ECG server is powered on\n")
ecg = pd.read_csv("../sample_data/samples.csv")
print("read sample data\n")

SAMPLES = 100
# t is the time dimension
t = ecg.iloc[:,0]  
# s is the actual signal value
signal = ecg.iloc[:,1]   
dt = t[1] - t[0]

counter_signal = 0

s = socket.socket()
host = socket.gethostname()
port = 58111

s.bind((host, port))
s.listen(5)

con, addr = s.accept()
print("Connection from: ", addr)
	
while(True):
	print("Sending batch")
#send the first 100 samples, that define 2 second in the given dataset.	
	to_send=b""	
	for i in range(0,100):
		print("adding sample: ",signal[counter_signal])
		b = struct.pack('d',signal[counter_signal])
		to_send+=b
		counter_signal+=1

	sended=con.send(to_send)
	time.sleep(1)	# sleep 1 second

