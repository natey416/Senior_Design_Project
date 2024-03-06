#!/usr/bin/env python3
import sys, time
import RPi.GPIO as GPIO

# pinlist and servo pin
gpioList = [7,11,12,13,15,16,18,19,21,22,23,24,26,29,31,33,35,36,37,38,40,8]
servoPin = 32

# setup Pi GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# setup PWM Pin
GPIO.setup(servoPin,GPIO.OUT)
pwm0 = GPIO.PWM(servoPin,50)
pwm0.start(2.5) #initial position
 
def repeat():
  global gpioList
  for i in gpioList:
    GPIO.setup(i,GPIO.OUT)
  while True:
    duty = 2.5
    for j in gpioList:
      duty = duty + (12.5-2.5)/22
      pwm0.ChangeDutyCycle(duty)
      GPIO.output(j,GPIO.HIGH)
      time.sleep(0.1)
    duty = 12.5
    for j in gpioList:
      duty = duty - (12.5-2.5)/22
      pwm0.ChangeDutyCycle(duty)
      GPIO.output(j,GPIO.LOW)
      time.sleep(0.1)
      
def setOff():
  global gpioList
  for i in gpioList:
    GPIO.output(i,GPIO.LOW)

if __name__ == '__main__':
  try:
    repeat()
  except KeyboardInterrupt:
    setOff()
    sys.exit(0)
