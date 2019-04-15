from twilio.rest import Client
import time
import serial


def text(message):
	account_sid = 'AC8f4a2e5f0a790599716abacda8dfce48'
	auth_token = '4e986817ca5b19fbc8d1d9ad7ee1fd7b'
	client = Client(account_sid, auth_token)
	message =  client.messages.create(to="+19136090625", from_="+19132988523", body= message)
	print('Message Sent!')


ser=serial.Serial(port='/dev/ttyUSB0',baudrate=9600,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=1)
while 1:
	x=ser.readline().strip('\n')
	try:
		y = x[9]
		y = str(y)
		if y == 'B':
			text("B is at the Door!")
		elif y == 'E':
			text("E is at the Door!")
	except IndexError:
		continue

