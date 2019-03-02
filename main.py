#!/usr/bin/python
import os, sys
from wallaby import *
from movement import *
from effectors import *
from wait_for_start import *
from constants import *

    
def main():  
  	create_connect()

  	#print "Connected to create!!"

  	msleep(5000)
 	#wait_for_light(LIGHT_SENSOR)
	"""    
 	if wait_for_start(LIGHT_SENSOR) == False:
		print("BAD CALIBRATION!!!")
		return False
	"""
 	shut_down_in(120)
  	enable_servos()
 	arm_back(50)
   	claw_open(50)
  	CCW(50, 35)

	#========================================================
   	#Get first supply stack!								=
	#========================================================
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
	#========================================================
   	#Get second supply stack!								=
	#========================================================
   	arm_up(50)
   	CCW(100,115)
  	arm_down(50)
	forward(100,195)
	CCW(50, 5) #gently turn into sencond supply stack
  	claw_close(50)
  	arm_up(50)
  	backward(100,140)
   	CW(100,165)
   	arm_down(25)
  	backward(100,120)
	msleep(1000) # sleep to calm the shakes
   	claw_open(50)
  	CW(50,5)
	#========================================================
   	#Get third supply stack!								=
	#========================================================
  	arm_up(50)
   	forward(100,55)
   	CCW(100, 62) # turn towards third pile
  	forward(100, 190)
  	arm_down(50)
   	CCW(50, 10)
	forward(50, 40)
  	claw_close(50) #  we got #3
	backward(50, 40)
   	arm_up(50)
  	CW(100, 65)
   	backward(100, 300)
   	arm_down(50)
  	claw_open(50)#scoring #3
 	CW(50,5)
	arm_up(50)
	#========================================================
   	#Get first water POMS!									=
	#========================================================
	#First realign
	backward(100, 100)
	CW(50, 85)
	forward(100, 600)# HIT THE PIPE!!!
     #realign done   

  	backward_to_black(300, 0, THRESH)
  	CCW(100, 90)
  	drive_to_bump(100) #hit pipe next to water container
   	msleep(1000)
 	forward(100, 340)
  	CCW(100, 90) #turn to face first water pile
  	arm_down(50)
  	forward(100, 75)
	CCW(50,15)
	forward(100,40)
  	claw_close(50)
   	backward(100, 75)
  	arm_up(50)
 	CW(100, 285)#turn to water reclamation unit first pom pile
	forward(50,90)#get on top of water unit
  	arm_score(25)
  	#turn_CCW_to_black(100,0, THRESH)
   	#drive_to_bump(100) 
  	#CW(100, 45)
 	claw_open(50)  #FIRST POMS SCORED!!!
	#========================================================
   	#Get second water POMS!							        =
	#========================================================
        
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
   	forward(100, 395)#go forward to water reclamation unit
	claw_open(50)#Just scored pile two
  	arm_up(50)

    
	#========================================================
   	#Go score third water POMS							    =
	#========================================================
 	backward(100,900) #turn tp pile 3
	CW(100,115)
  	backward(100,90)
  	arm_down(50)
  	forward(100,75)
  	claw_close(50)
  	backward(100,75)
  	arm_score(50)
  	CCW(100,115)
  	forward(100,890)
	#========================================================
   	#Now push water bin!							=
	#========================================================
   	CW(100,10)
 	claw_open(50)
  	CW(100,5)
  	arm_down(50)
   	CCW(100,35)

  	disable_servos()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
