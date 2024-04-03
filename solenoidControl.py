#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

class solenoidCtrl():
  def __init__(self):
    self.deadzone = 0.20
    self.deadMax = 0.80
    toggleFreqMax = 10 #hz
    self.thrustEqn = toggleFreqMax/self.deadMax
    self.gpioList = [7,11,12,13,15,16,18,19,21,22,23,24,26,29,31,33,35,36,37,38,40,8]
    self.servoPin = 32
    # Thruster maps to pins
    self.APHX = 7
    self.APLX = 11
    self.ASHX = 12
    self.ASLX = 13
    self.FPX = 15
    self.FSX = 16
    self.APHY = 18
    self.APLY = 19
    self.ASHY = 21
    self.ASLY = 22
    self.FPHY = 23
    self.FSHY = 24
    self.FPLY = 26
    self.FSLY = 29
    self.APHZ = 31
    self.APLZ = 33
    self.ASHZ = 35
    self.ASLZ = 36
    self.FPHZ = 37
    self.FSHZ = 38
    self.FPLZ = 40
    self.FSLZ = 8
    # Channel maps to translation axes
    self.xB = [self.APHX,self.APLX,self.ASHX,self.ASLX]
    self.xF = [self.FPX,self.FSX]
    self.yL = [self.APHY,self.APLY,self.FPHY,self.FPLY]
    self.yR = [self.ASHY,self.ASLY,self.FSHY,self.FSLY]
    self.zT = [self.APHZ,self.ASHZ,self.FPHZ,self.FSHZ]
    self.zB = [self.APLZ,self.ASLZ,self.FPLZ,self.FSLZ]
    # Channel maps to rotation axes
    self.zCW = [self.FPHY,self.FPLY,self.ASHY,self.ASLY]
    self.zCCW = [self.FSHY,self.FSLY,self.APHY,self.APLY]
    self.xCW = [self.FSHZ,self.ASHZ,self.FPLZ,self.APLZ]
    self.xCCW = [self.FPHZ,self.APHZ,self.FSLZ,self.ASLZ]
    self.yCW = [self.FPX,self.FSX,self.APLX,self.ASLX]
    self.yCCW = [self.FPX,self.FSX,self.APHX,self.ASHX]
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    for i in self.gpioList:
      GPIO.setup(i,GPIO.OUT)
    
    GPIO.setup(self.servoPin,GPIO.OUT)
    self.pwm0 = GPIO.PWM(self.servoPin,50)
    self.pwm0.start(1.5) #initial position    

  def setOff(self):
    for i in self.gpioList:
      GPIO.output(i,GPIO.LOW)
    
  def turnOn(self,pins):
    for i in pins:
      GPIO.output(i,GPIO.HIGH)
  def turnOff(self,pins):
    for i in pins:
      GPIO.output(i,GPIO.LOW)
      
  def varCtrl(self,axis,pins):
    if axis < self.deadzone:
      for i in pins:
        GPIO.output(i,GPIO.LOW)
    elif axis > self.deadMax:
      for i in pins:
        GPIO.output(i,GPIO.HIGH)
    else:
      frequency = self.thrustEqn * axis
      for i in pins:
        GPIO.output(i,GPIO.HIGH)
      time.sleep(1/frequency/2)
      for i in pins:
        GPIO.output(i,GPIO.LOW)
      time.sleep(1/frequency/2)
    
  def setServo(self,percent):
    self.pwm0.ChangeDutyCycle(percent)
