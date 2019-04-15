#When an RFID card is scanned or a button is pushed, a text message is sent and an LED lights up
from twilio.rest import Client
import time
import serial
import RPi.GPIO as GPIO

#Configure the GPIO pins
#Pin 18 = LED
#Pin 23 = Button
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)

#Function to send text message and pause for 5 seconds for LED
def text(message):
	account_sid = 'AC8f4a2e5f0a790599716abacda8dfce48'
	auth_token = '4e986817ca5b19fbc8d1d9ad7ee1fd7b'
	client = Client(account_sid, auth_token)
	message =  client.messages.create(to="+19136090625", from_="+19132988523", body= message)
	print('Message Sent!')
	time.sleep(5.0)

#Enable serial port for the RFID scanner
ser=serial.Serial(port='/dev/ttyUSB0',baudrate=9600,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=0.1)

while 1:
	#Read serial port
	x=ser.readline().strip('\n')

	try:
		#Turn LED off
		GPIO.output(18,GPIO.LOW)

		#Read Button State
		inputstate = GPIO.input(23)

		#If the button was pressed, turn on LED and send text
		if inputstate == True:
			print("Button")
			GPIO.output(18,GPIO.HIGH)
			text("Button is at the Door!")

		#Reading RFID data
		y = x[9]
		y = str(y)
		print(y)

		#Send text based on which card, light LED
		if y == 'B':
			GPIO.output(18,GPIO.HIGH)
			text("B is at the Door!")
		elif y == 'E':
			GPIO.output(18,GPIO.HIGH)
			text("E is at the Door!")

	#Catch error when no card is scanned
	except IndexError:
		continue
