#! /usr/bin/env python3

from gazebo_msgs.msg import LinkStates, ModelStates, LinkState, ModelState
from std_msgs.msg import String
import rospy
from time import sleep
from geometry_msgs.msg import Twist

rospy.init_node("experiemtnal_shit")

drone = rospy.Publisher("/gazebo/set_link_state", LinkState, queue_size=10)

takeoff1 = LinkState()
takeoff2 = LinkState()
takeoff3 = LinkState()
takeoff4 = LinkState()

takeoff1.link_name = "propeller1"
takeoff1.reference_frame = "world"
takeoff1.twist.linear.z = 1

takeoff2.link_name = "propeller2"
takeoff2.reference_frame = "world"
takeoff2.twist.linear.z = 1

takeoff3.link_name = "propeller3"
takeoff3.reference_frame = "world"
takeoff3.twist.linear.z = 1

takeoff4.link_name = "propeller4"
takeoff4.reference_frame = "world"
takeoff4.twist.linear.z = 1



while not rospy.is_shutdown():
    drone.publish(takeoff1)
    drone.publish(takeoff2)
    drone.publish(takeoff3)
    drone.publish(takeoff4)

