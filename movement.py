#!/usr/bin/python
import os, sys
from wallaby import *

#Created Wednesday, February 6th, 2019. Creators: Kade Little, Soham Kinkhbwala, and Aditya Patra.

#Function: backward
#Description: move backward at a certain speed a certain distance
#Arguments:
	#speed = speed the robot moves
	#mm = distance in mm to move

def backward(speed, mm):
   	
	set_create_distance(0);
	create_drive_straight(speed);
	while(get_create_distance() < mm):
		pass
  	create_drive_straight(0)

#Function: forward
#Description: move forward at a certain speed a certain distance
#Arguments:
	#speed = speed the robot moves
	#mm = distance in mm to move

def forward (speed, mm):
    
	set_create_distance(0)
	create_drive_straight(-speed)
	while(get_create_distance() > -mm):
		pass
 	create_drive_straight(0)

def CCW(speed, angle):
    
	set_create_total_angle(0)
	create_spin_CW(speed)
	while(get_create_total_angle() >= -angle):
		pass
 	create_spin_CW(0)
        
def CW(speed, angle):
    
	set_create_total_angle(0)
	create_spin_CCW(speed)
	while(get_create_total_angle() < angle):
		pass
	create_spin_CCW(0)
	
def forward_to_black(speed, port, thresh):
	create_drive_straight(-speed)
	while(analog(port) <= thresh):
		pass
 	create_drive_straight(0)

def backward_to_black(speed,port,thresh):
	create_drive_straight(speed)
	while(analog(port) <= thresh):
		pass
  	create_drive_straight(0)
            
def turn_CW_to_black(speed, port, thresh):
	create_spin_CW(speed)
	while(analog(port) <= thresh):
		pass
 	create_spin_CW(0)

def turn_CCW_to_black(speed, port, thresh):
	create_spin_CCW(speed)
	while(analog(port) <= thresh):
		pass
 	create_spin_CCW(0)
