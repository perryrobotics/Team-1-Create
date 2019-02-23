#!/usr/bin/python
import os, sys
from wallaby import *
from movement import *
from effectors import *
from wait_for_start import *

LIGHT_SENSOR = 1
    
def main():  
  	create_connect()

  	#print "Connected to create!!"

  	#msleep(5000)
 	#wait_for_light(LIGHT_SENSOR)
        
 	if wait_for_start(LIGHT_SENSOR) == False:
		print("BAD CALIBRATION!!!")
		return False
        
 	shut_down_in(120)
  	enable_servos()
 	arm_back(50)
   	claw_open(50)
  	CCW(50, 35)

   	#Get first supply stack!
   	arm_down(50)
   	forward(100, 135)
   	claw_close(50)
   	arm_up(50)
 	forward(100,100) #get out of the way of the wallaby
   	backward(100,190)
   	CW(100,90)
   	backward(100, 100)
   	arm_down(50)
   	claw_open(50)
   	#Got first supply stack, onto getting the second!
   	arm_up(50)
   	CCW(225,109)
  	arm_down(50)
	forward(100,175)
  	claw_close(50)
  	arm_up(50)
  	backward(100,140)
   	CW(225,140)
   	arm_down(25)
  	backward(100,120)
   	claw_open(50)
  	#Got second supply stack, now onto the last supply stack!
  	arm_up(50)
   	forward(200,55)
   	CCW(200, 42)
  	forward(100, 190)
  	arm_down(50)
   	CCW(50, 10)
	forward(50, 20)
  	claw_close(50)
	backward(50, 20)
   	arm_up(50)
  	CW(300, 50)
   	backward(200, 175)
   	arm_down(50)
   	arm_down(50)
  	claw_open(50)
	arm_up(50)
	backward(100, 100)
	CW(50, 85)
	forward(100, 400)# HIT THE PIPE!!!
        
  	#GO GET BLUE POMS!!
  	backward_to_black(300, 0, 2700)
  	CCW(100, 90)
  	drive_to_bump(100)
   	msleep(1000)
 	forward(100, 300)
  	CCW(100, 90)
  	arm_down(50)
  	forward(100, 40)
  	claw_close(50)
   	backward(100, 50)
  	arm_up(50)
 	CW(100, 268)#turn to water reclamation unit
  	arm_score(25)
  	#turn_CCW_to_black(100,0, THRESH)
   	#drive_to_bump(100) 
  	#CW(100, 45)
 	claw_open(50)  #FIRST POMS SCORED!!!
   	# GO GET SECOND POM PILE!!!
        
 	backward(100, 350)
  	CW(100, 90)
  	backward(100, 100)
  	CW(100, 40)# Align the second poms
   	backward(100, 20)
   	arm_down(50)
   	forward(100, 65)
   	claw_close(50)
   	backward(100, 50)
   	arm_score(50)
	CCW(100,125)
   	forward(100, 365)#go forward to water reclamation unit
	claw_open(50)#Just scored pile two
  	arm_up(50)

    
    #go score pile three 
 	backward(100,900)
	CW(100,115)
  	backward(100,90)
  	arm_down(50)
  	forward(100,75)
  	claw_close(50)
  	backward(100,75)
  	arm_score(50)
  	CCW(100,115)
  	forward(100,890)
   	CW(100,10)
 	claw_open(50)
  	CW(100,5)
  	arm_down(50)
   	CCW(100,35)
   	
        
        

  	disable_servos()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
