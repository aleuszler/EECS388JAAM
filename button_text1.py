import RPi.GPIO as GPIO
import time
from twilio.rest import Client
GPIO.setwarnings(False)
def text():
	account_sid = '###'
	auth_token = '###'
	client = Client(account_sid, auth_token)
	message =  client.messages.create(to="###", from_="###", body="Hello from Python!")
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
