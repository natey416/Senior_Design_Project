#!/usr/bin/python3
import sys, time
import RPi.GPIO as GPIO
import pigpio

# pinlist and servo pin
gpioList = [7,11,12,13,15,16,18,19,21,22,23,24,26,29,31,33,35,36,37,38,40,8]
servoPin = 12

# setup Pi GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# setup PWM Pin
pwm = pigpio.pi()
pwm.set_mode(servoPin, pigpio.OUTPUT)
pwm.set_PWM_frequency(servoPin,50)
 
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
      
def repeat2():
  global gpioList
  for i in gpioList:
    GPIO.setup(i,GPIO.OUT)
  pin = 12
  while True:
    frequency = 10
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1/frequency/2)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1/frequency/2)

def repeat3():
  pwm.set_servo_pulsewidth(servoPin,500)
  time.sleep(5)
  pwm.set_servo_pulsewidth(servoPin,1500)
  time.sleep(5)
  pwm.set_servo_pulsewidth(servoPin,2000)
  time.sleep(5)
  pwm.set_servo_pulsewidth(servoPin,2500)
  time.sleep(5)
      
def setOff():
  global gpioList, servoPin
  for i in gpioList:
    GPIO.output(i,GPIO.LOW)
  pwm.set_PWM_dutycycle(servoPin,0)
  pwm.set_PWM_frequency(servoPin,0)

if __name__ == '__main__':
  try:
    repeat3()
  except KeyboardInterrupt:
    setOff()
    sys.exit(0)
