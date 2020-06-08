import socket
import struct
import numpy as np
import ecg_plot as ep
import matplotlib.pyplot as plt
from scipy import signal, misc
from scipy.fftpack import fft, ifft, fftfreq

SAMPLES = 100
# data domain
t1 = np.zeros([SAMPLES,1])
#init time domain
tval = 0.000

for i in range(0,SAMPLES):
	t1[i,0] = tval
	tval+=0.004

s1 = np.zeros([SAMPLES, 1])
s = socket.socket()
host = socket.gethostname()
port = 58111
print("Connecting to ECG server")

s.connect((host, port))

while(True):

	run = 0
	print("Received from server:\n")
	data_batch = s.recv(1024)

	#composing the samples received back into doubles.
	for i in range(0,SAMPLES):
		b=b""	

		for k in range(0,8):
			b += data_batch[8*run+k].to_bytes(1,byteorder='big')
	
		s1[run, 0], = struct.unpack('d', b) 
		#print("Value composed: ", s1[0,run])
		run += 1

	print(s1)
	#plot
	plt.plot(t1, s1)
	plt.grid(color='r', linestyle='-', linewidth=0.5)	
	axes = plt.gca()
	axes.set_facecolor((0.9, 0.88, 0.75))
	axes.set_ylim([-1,1.2])
	plt.rcParams['figure.figsize'] = [10 ,4]
	plt.title('ECG Signal received from Server')
	plt.xlabel('Time(seconds)')
	plt.ylabel('ECG(mV)')
	plt.pause(1)
	plt.cla()
plt.show()

	
