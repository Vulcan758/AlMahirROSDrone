#! /usr/bin/env python3

import pygame
from time import sleep 
import rospy
from std_msgs.msg import String

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("rover controller")
rospy.init_node("drone_controller")

up = 119
down = 115
left = 97
right = 100

takeoff = pygame.K_t
land = pygame.K_q
right_arr = pygame.K_RIGHT
left_arr = pygame.K_LEFT


directions = [up, down, left, right, right_arr, left_arr, takeoff, land]
dir_states = [False, False, False, False, False, False, False, False]
outputs = ["w", "s", "a", "d", "right_arr", "left_arr", "t", "q"]

def controller():
    drone_out = rospy.Publisher("/drone_keys", String, queue_size=10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed = directions.index(event.key)
                dir_states[pressed] = True
            elif event.type == pygame.KEYUP:
                released = directions.index(event.key)
                dir_states[released] = False
        for dir in dir_states:
            if dir == True:
                print(outputs[dir_states.index(dir)])
                drone_out.publish(outputs[dir_states.index(dir)])
        sleep(0.1)
            
if __name__ == "__main__":
    controller()

#w --> 119
#a --> 97
#s --> 115
#d --> 100