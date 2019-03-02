#!/usr/bin/python
import os, sys
from wallaby import *
from constants import *
    
def move_servo_slow(port, current_pos, end_pos,step):
	if end_pos < current_pos:
		step = -step
	for pos in range(current_pos, end_pos, step):
		set_servo_position(port, pos)
  		msleep(40)
	set_servo_position(port,end_pos)
            
            
def arm_up(step):
	move_servo_slow(ARM_PORT, get_servo_position(ARM_PORT), ARM_U, step)
        
def arm_down(step):
	move_servo_slow(ARM_PORT, get_servo_position(ARM_PORT), ARM_D, step)
        
def arm_back(step):
	move_servo_slow(ARM_PORT, get_servo_position(ARM_PORT), ARM_B, step)
  
def arm_score(step):
	move_servo_slow(ARM_PORT, get_servo_position(ARM_PORT), ARM_S, step)
        
def claw_open(step):
	move_servo_slow(CLAW_PORT, get_servo_position(CLAW_PORT), CLAW_O, step)
        
def claw_close(step):
	move_servo_slow(CLAW_PORT, get_servo_position(CLAW_PORT), CLAW_C, step)
        
        
        
            






