#!/usr/bin/env python3
import RPi.GPIO as GPIO

class solenoidCtrl():
  def __init__(self):
    self.gpioList = [7,11,12,13,15,16,18,19,21,22,23,24,26,29,31,33,35,36,37,38,40,8]
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
    # Channel maps to thrusters
    self.xB = [self.APHX,self.APLX,self.ASHX,self.ASLX]
    self.xF = [self.FPX,self.FSX]
    self.yL = [self.APHY,self.APLY,self.FPHY,self.FPLY]
    self.yR = [self.ASHY,self.ASLY,self.FSHY,self.FSLY]
    self.zT = [self.APHZ,self.ASHZ,self.FPHZ,self.FSHZ]
    self.zB = [self.APLZ,self.ASLZ,self.FPLZ,self.FSLZ]
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    for i in self.gpioList:
      GPIO.setup(i,GPIO.OUT)

  def setOff(self):
    for i in self.gpioList:
      GPIO.output(i,GPIO.LOW)
    
  def turnOn(self,pins):
    for i in pins:
      GPIO.output(i,GPIO.HIGH)
  def turnOff(self,pins):
    for i in pins:
      GPIO.output(i,GPIO.LOW)
