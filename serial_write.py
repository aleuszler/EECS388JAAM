#import serial
#import time

#device = serial.Serial("/dev/ttyUSB0", 9600)

#while True:
#	print (device.read(12))
#	time.sleep(1)

#device.write("ver")
#device.read(12)

import time
import serial

ser = serial.Serial(port = '/dev/ttyAMA0', baudrate =9600, parity = serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
counter = 0
while 1:
	ser.write('Write counter: %d \n'%(counter))
	time.sleep(1)
	counter += 1 
