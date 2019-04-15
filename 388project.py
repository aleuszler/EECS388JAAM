import RPi.GPIO as GPIO
import time
from twilio.rest import Client
GPIO.setwarnings(False)
def text():
	account_sid = 'AC8f4a2e5f0a790599716abacda8dfce48'
	auth_token = '4e986817ca5b19fbc8d1d9ad7ee1fd7b'
	client = Client(account_sid, auth_token)
	message =  client.messages.create(to="+19136090625", from_="+19132988523", body="Hello from Python!")
	print('Message Sent!')
	time.sleep(5.0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)

while True:
	GPIO.output(18,GPIO.LOW)
	inputstate = GPIO.input(23)
	if inputstate == False:
		x = 3
	else:
		GPIO.output(18,GPIO.HIGH)
		text()
