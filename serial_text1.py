from twilio.rest import Client
import time
import serial


def text(message):
	account_sid = '###'
	auth_token = '###'
	client = Client(account_sid, auth_token)
	message =  client.messages.create(to="###", from_="###", body= message)
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

