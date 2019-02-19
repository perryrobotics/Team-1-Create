#!/usr/bin/python
import os, sys
from wallaby import *
from movement import *
from effectors import *

def main():  
  	create_connect()
  	enable_servos()
  	print "Connected to create!!"
  	arm_back(50)
   	claw_open(50)
  	msleep(5000)
   	#Get first supply stack!
   	arm_down(50)
   	forward(100, 135)
   	claw_close(25)
   	arm_up(25)
   	backward(100,90)
   	CW(100,90)
   	backward(100, 100)
   	arm_down(50)
   	claw_open(25)
   	#Got first supply stack, onto getting the second!
   	arm_up(50)
   	CCW(225,109)
  	arm_down(50)
	forward(100,175)
  	claw_close(25)
  	arm_up(25)
  	backward(100,140)
   	CW(225,140)
   	arm_down(25)
  	backward(100,120)
   	claw_open(25)
  	#Got second supply stack, now onto the last supply stack!
  	arm_up(50)
   	forward(200, 45)
   	CCW(200, 42)
  	forward(200, 190)
  	arm_down(25)
   	CCW(50, 10)
  	claw_close(25)
   	arm_up(25)
  	CW(300, 50)
   	backward(200, 175)
   	arm_down(50)
   	arm_down(25)
  	claw_open(25)
	arm_up(25)
	backward(100, 150)
	CW(50, 95)
	forward(100, 330)
        
  	#GO GET BLUE POMS!!
  	backward_to_black(300, 0, 2700)
	CW(50, 173)
	forward(100, 172)
	arm_down(25)
	claw_close(25)
	arm_up(25)
	turn_CW_to_black(50,0, 2750)
	forward(100, 167)
	CCW(100, 22)
	forward(100, 105)
	move_servo_slow(3, 900, 670, 50)
	claw_open(25)
	backward(100,120)
	CW(100,20)
	arm_back(50)
	forward(100, 200)
	CW(100,90)
	forward(100,700)
	backward_to_black(300, 0, 2700)
	CW(100, 105)
	forward(100, 700)
	CCW(100,110)
	backward(100, 230)
	forward(100, 50)
	arm_down(25)
	claw_close(25)
	arm_back(25)
	forward_to_black(300,0,2700)
	CCW(100,100)
	forward(200, 500)
	move_servo_slow(3, 900, 670, 50)
	claw_open(25)
	
	
    
	
    
   
  	
 	
  	create_disconnect()
  	disable_servos()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
