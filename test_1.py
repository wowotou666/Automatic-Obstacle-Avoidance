from AlphaBot import AlphaBot
import RPi.GPIO as GPIO
Ab = AlphaBot()
try:
	while True:
    		Ab.left()
except:
	GPIO.cleanup()
