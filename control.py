#!/usr/bin/env python3
import sys, time, pygame
import RPi.GPIO as GPIO
from solenoidControl import solenoidCtrl

# pygame setup
background_color = (255,0,0)
screen = pygame.display.set_mode((200,200))
pygame.display.set_caption('Group 2 Control')
screen.fill(background_color)
pygame.display.flip()

# pinlist and servo pin
servoPin = 32

def repeat(sol):
  Running = True
  while Running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        Running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          sol.turnOn(sol.xB)
        elif event.key == pygame.K_DOWN:
          sol.turnOn(sol.xF)
        elif event.key == pygame.K_LEFT:
            sol.turnOn(sol.yL)
        elif event.key == pygame.K_RIGHT:
            sol.turnOn(sol.yR)
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          sol.turnOff(sol.xB)
        elif event.key == pygame.K_DOWN:
          sol.turnOff(sol.xF)
        elif event.key == pygame.K_LEFT:
            sol.turnOff(sol.yL)
        elif event.key == pygame.K_RIGHT:
            sol.turnOff(sol.yR)

if __name__ == '__main__':
  try:
    sol = solenoidCtrl()
    # setup PWM Pin
    GPIO.setup(servoPin,GPIO.OUT)
    pwm0 = GPIO.PWM(servoPin,50)
    pwm0.start(2.5) #initial position
    repeat(sol)
  except KeyboardInterrupt:
    sol.setOff()
    sys.exit(0)
