#!/usr/bin/python
import os, sys
from wallaby import *

def wait_for_start(port):      
	print("LIGHT OFF NOW!!!.  Press A when ready!")
 	msleep(2000)
  	while not a_button():
		off = analog(port)
		print ("OFF: ",analog(port) )
 	print ("LIGHT OFF VALUE: ", off)
	if off <1500:
		print ("BAD CALIBRATION!!!  DO NOT RUN!!!")
		return 0
 	while a_button():
		pass
	
	print("LIGHT ON NOW!!!.  Press B when ready!")
  	while not b_button():
		on = analog(port)
		print ("ON: ",analog(port) )
 	print ("LIGHT ON VALUE: ", on)
	if on >1000:
		print ("BAD CALIBRATION!!!  DO NOT RUN!!!")
		return 0

	print("GOOD CALIBRATION!  LETS GO!!!")
	print ("TURN LIGHT OFF NOW!!!! PRESS C WHEN READY")
  	while c_button()==0:
		pass
   
	thresh = (off + on)/2
	while analog(port) > thresh:
		print ("WAITING FOR LIGHT!!!")
		pass
