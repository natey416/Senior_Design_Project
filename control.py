#!/usr/bin/env python3
import sys, time
import RPi.GPIO as GPIO

# pinlist and servo pin
gpioList = [7,11,12,13,15,16,18,19,21,22,23,24,26,29,31,33,35,36,37,38,40,8]
xB = [7,11,12,13]
xF = [15,16]
yL = [18,19,23,26]
yR = [21,22,24,29]
zT = [31,35,37,38]
zB = [33,36,40,8]
servoPin = 32

# setup Pi GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# setup PWM Pin
GPIO.setup(servoPin,GPIO.OUT)
pwm0 = GPIO.PWM(servoPin,50)
pwm0.start(2.5) #initial position

def setOff():
  global gpioList
  for i in gpioList:
    GPIO.output(i,GPIO.LOW)
    
def turnOn(pins):
	for i in pins:
		GPIO.output(i,GPIO.HIGH)

def repeat():
	global gpioList,xB,xF,yL,yR,zT,zB
	for i in gpioList:
		GPIO.setup(i,GPIO.OUT)
	while True:
		

if __name__ == '__main__':
  try:
    repeat()
  except KeyboardInterrupt:
    setOff()
    sys.exit(0)
