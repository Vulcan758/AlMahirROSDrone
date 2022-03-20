#! /usr/bin/env python3

from gazebo_msgs.msg import LinkStates, ModelStates, LinkState, ModelState
import rospy
from time import sleep
from geometry_msgs.msg import Twist

rospy.init_node("takeoff_plugin")

model = "drone"

takeoff = ModelState()

ref = "world"
"""
takeoff.pose.position.z = 2
takeoff.model_name = model
takeoff.reference_frame = ref
"""
takeoff = ModelState()
takeoff.model_name = model
takeoff.reference_frame = ref

takeoff.twist.linear.z = 4

drone = rospy.Publisher("/gazebo/set_model_state", ModelState, queue_size=10)

while not rospy.is_shutdown():
    yo = input("give input bro > ")
    if yo == "w":
        for i in range(5):
            drone.publish(takeoff)
        
    else:
        pass