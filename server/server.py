import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import socket
import struct #pack in double to send over network
import time
import threading

SAMPLES = 100

class ClientThread(threading.Thread):
	def __init__(self, clientAddress, clientsocket):
		threading.Thread.__init__(self)
		self.csocket = clientsocket
		print("new connection added: ", clientAddress)

	def run(self):
		
		ecg = pd.read_csv("../sample_data/samples.csv")
		# t is the time dimension
		t = ecg.iloc[:,0]  
		# s is the actual signal value
		signal = ecg.iloc[:,1]   
		counter_signal = 0
		cs = con
		
		while(True):
			print(self)
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

##########################################################################
##########################################################################
##########################################################################
#		Multithreaded server program				 #
#		Mouzakitis Nikolaos, Grenoble 2020.			 #
#									 #
##########################################################################
##########################################################################
##########################################################################

print("ECG server is powered on\n")
print("read sample data\n")

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 58111
s.bind((host, port))
	
while(True):
	s.listen(5)

	(con, (addr,port)) = s.accept()
	newthread = ClientThread(addr, port)	
	newthread.start()

