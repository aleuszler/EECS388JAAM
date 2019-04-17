import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #blue button
GPIO.setup(10,GPIO.OUT) #blue LED
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #yellow button
GPIO.setup(9, GPIO.OUT) #yellow LED
GPIO.setup(11, GPIO.OUT)

GPIO.output(11,GPIO.HIGH)
while True:
	GPIO.output(10,GPIO.LOW)
	GPIO.output(9,GPIO.LOW)
	blue = GPIO.input(23)
	yellow = GPIO.input(24)
	if yellow == False:
		GPIO.output(9,GPIO.HIGH)
		print("yellow")
	if blue == False:
		GPIO.output(10,GPIO.HIGH)
		print("blue")
	time.sleep(1.0)

