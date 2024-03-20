#!/usr/bin/env python3
import RPi.GPIO as GPIO

class solenoidCtrl():
  def __init__(self):
    self.gpioList = [7,11,12,13,15,16,18,19,21,22,23,24,26,29,31,33,35,36,37,38,40,8]
    self.APHX = 7
    self.APLX = 11
    self.ASHX = 12
    self.ASLX = 13
    self.FPX = 15
    self.FSX = 16
    self.xB = [7,11,12,13]
    self.xF = [15,16]
    self.yL = [18,19,23,26]
    self.yR = [21,22,24,29]
    self.zT = [31,35,37,38]
    self.zB = [33,36,40,8]
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
