import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

print("Encendiendo LED...")
GPIO.output(17, GPIO.HIGH)
time.sleep(2)

print("Apagando LED...")
GPIO.output(17, GPIO.LOW)

GPIO.cleanup()
