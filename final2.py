#When an RFID card is scanned or a button is pushed, a text message is sent and an LED lights up
from twilio.rest import Client
import time
import serial
import RPi.GPIO as GPIO

#Configure the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #blue button
GPIO.setup(10,GPIO.OUT) #blue LED
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #yellow button
GPIO.setup(9, GPIO.OUT) #yellow LED
GPIO.setup(11, GPIO.OUT) #green LED for RFID

#Function to send text message and pause for 5 seconds for LED
def text(message):
	account_sid = '###'
	auth_token = '###'
	client = Client(account_sid, auth_token)
	message =  client.messages.create(to="###", from_="###", body= message)
	print('Message Sent!')
	time.sleep(5.0)

#Enable serial port for the RFID scanner
ser=serial.Serial(port='/dev/ttyUSB0',baudrate=9600,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=0.1)

while 1:
	#Read serial port
	x=ser.readline().strip('\n')

	try:
		#Turn LED off
		GPIO.output(10,GPIO.LOW)
		GPIO.output(9,GPIO.LOW)
		GPIO.output(11,GPIO.LOW)

		#Read Button State
		Blue = GPIO.input(23)
		Yellow = GPIO.input(24)

		#If the button was pressed, turn on LED and send text
		if Blue == False:
			print("Blue Button")
			GPIO.output(10,GPIO.HIGH)
			text("Someone is at the blue door!")
		if Yellow == False:
			print("Yellow Button")
			GPIO.output(9,GPIO.HIGH)
			text("Someone is at the yellow door!")

		#Reading RFID data
		y = x[9]
		y = str(y)
		print(y)

		#Send text based on which card, light LED
		if y == 'B':
			GPIO.output(11,GPIO.HIGH)
			text("B is at the Door!")
		elif y == 'E':
			GPIO.output(11,GPIO.HIGH)
			text("E is at the Door!")

	#Catch error when no card is scanned
	except IndexError:
		continue
