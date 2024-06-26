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
  joysticks = {}
  stick_values = [0] * 6
  
  while Running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        Running = False
        
      if event.type == pygame.JOYDEVICEADDED:
        joy = pygame.joystick.Joystick(event.device_index)
        joysticks[joy.get_instance_id()] = joy
        print(f"Joystick {joy.get_instance_id()} connected. {joy.get_numaxes()} axes detected")
      if event.type == pygame.JOYDEVICEREMOVED:
        del joysticks[event.instance_id]
        print(f"Joystick {event.instance_id} disconnected")
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          sol.turnOn(sol.xB)
        elif event.key == pygame.K_DOWN:
          sol.turnOn(sol.xF)
        elif event.key == pygame.K_LEFT:
            sol.turnOn(sol.yL)
        elif event.key == pygame.K_RIGHT:
            sol.turnOn(sol.yR)
        elif event.key == pygame.K_w:
            sol.turnOn(sol.zB)
        elif event.key == pygame.K_s:
            sol.turnOn(sol.zT)
            
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          sol.turnOff(sol.xB)
        elif event.key == pygame.K_DOWN:
          sol.turnOff(sol.xF)
        elif event.key == pygame.K_LEFT:
            sol.turnOff(sol.yL)
        elif event.key == pygame.K_RIGHT:
            sol.turnOff(sol.yR)
        elif event.key == pygame.K_w:
            sol.turnOff(sol.zB)
        elif event.key == pygame.K_s:
            sol.turnOff(sol.zT)
            
    for joystick in joysticks.values():
      axes = joystick.get_numaxes()
      for i in range(axes):
        stick_values[i] = round(joystick.get_axis(i),2)
      button0 = joystick.get_button(0)

    if stick_values[4] < 0:
      sol.varCtrl(abs(stick_values[4]),sol.xB)
      sol.turnOff(sol.xF)
    elif stick_values[4] > 0:
      sol.varCtrl(stick_values[4],sol.xF)
      sol.turnOff(sol.xB)
      
    if stick_values[3] < 0:
      sol.varCtrl(abs(stick_values[3]),sol.yL)
      sol.turnOff(sol.yR)
    elif stick_values[3] > 0:
      sol.varCtrl(stick_values[3],sol.yR)
      sol.turnOff(sol.yL)
    
    if stick_values[0] < 0:
      sol.varCtrl(abs(stick_values[0]),sol.zCCW)
      sol.turnOff(sol.zCW)
    elif stick_values[0] > 0:
      sol.varCtrl(stick_values[0],sol.zCW)
      sol.turnOff(sol.zCCW)
    
    if stick_values[1] < 0:
      sol.varCtrl(abs(stick_values[1]),sol.zB)
      sol.turnOff(sol.zT)
    if stick_values[1] > 0:
      sol.varCtrl(stick_values[1],sol.zT)
      sol.turnOff(sol.zB)
    
    if stick_values[0] == 0 and stick_values[1] == 0 and stick_values[3] == 0 and stick_values[4] == 0:
      sol.setOff()
    
    if button0 == 1:
      sol.setServo(2500)
    else:
      sol.setServo(1000)
    
    pygame.display.flip()

if __name__ == '__main__':
  try:
    sol = solenoidCtrl()
    
    pygame.joystick.init()
    
    repeat(sol)
  except KeyboardInterrupt:
    sol.setOff()
    pygame.quit()
    sys.exit(0)
