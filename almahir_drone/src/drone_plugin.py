#! /usr/bin/env python3
from xml.sax.handler import feature_external_pes
from gazebo_msgs.msg import LinkStates, ModelStates, LinkState, ModelState
from std_msgs.msg import String
import rospy
from time import sleep
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler


model = "drone"
ref = "world"

class Drone():
    def __init__(self, model, ref):
        rospy.init_node("drone_plugin")
        self.model = "drone"
        self.drone = rospy.Publisher("/gazebo/set_model_state", ModelState, queue_size=10)
        self.orient = rospy.Subscriber("/gazebo/model_states", ModelStates, self.orient_callback)
        self.takeoff = ModelState()
        self.takeoff.model_name = model
        self.takeoff.reference_frame = ref

        #self.takeoff.twist.linear.z = 5

        self.takeoff.pose.position.z = 0
        self.takeoff.pose.position.x = 0
        self.takeoff.pose.position.y = 0


        self.takeoff_state = False
        self.forward_state = False
        self.backward_state = False
        self.left_state = False
        self.right_state = False
        self.yaw_right_state = False
        self.yaw_left_state = False

        self.increment = 0.05

        self.drone_inp = rospy.Subscriber("/drone_keys", String, self.drone_callback)

        self.rate = rospy.Rate(50)
        self.current_euler = None


    def drone_callback(self, data):
        inp = data.data

        if self.takeoff_state == True and inp == "t":
            print("drone is already in the air")
            rospy.loginfo("drone is already in the air")
        if inp == "t":
            self.smooth_rise()
            self.takeoff.pose.position.z += 1
            self.takeoff_state = True   
        if inp == "w":
            self.takeoff.pose.position.x += self.increment
            self.forward_state = True
        if inp == "s":
            self.takeoff.pose.position.x -= self.increment
            self.backward_state = True
        if inp == "a":
            self.takeoff.pose.position.y += self.increment
            self.left_state = True
        if inp == "d":
            self.takeoff.pose.position.y -= self.increment
            self.right_state = True
        if inp == "q":
            self.takeoff.pose.position.z = 0
            self.takeoff_state = False
        if inp == "right_arr":
            #self.current_euler[0] += 0.1
            self.target_quaternion = quaternion_from_euler(self.current_euler[0], self.current_euler[1], self.current_euler[2] + 0.1)
            self.takeoff.pose.orientation.x = self.target_quaternion[0]
            self.takeoff.pose.orientation.y = self.target_quaternion[1]
            self.takeoff.pose.orientation.z = self.target_quaternion[2]
            self.takeoff.pose.orientation.w = self.target_quaternion[3]
            self.yaw_right_state = True

        if inp == "left_arr":
            self.target_quaternion = quaternion_from_euler(self.current_euler[0], self.current_euler[1], self.current_euler[2] - 0.1)
            self.takeoff.pose.orientation.x = self.target_quaternion[0]
            self.takeoff.pose.orientation.y = self.target_quaternion[1]
            self.takeoff.pose.orientation.z = self.target_quaternion[2]
            self.takeoff.pose.orientation.w = self.target_quaternion[3]
            self.yaw_right_state = True
        else:
            pass

    def orient_callback(self, data):
        model_pose = data.pose[1]
        orientation = model_pose.orientation
        current_orientation = [orientation.x, orientation.y, orientation.z, orientation.w]
        roll, pitch, yaw = euler_from_quaternion(current_orientation)
        #print(data)
        self.current_euler = [roll, pitch, yaw] #euler_from_quaternion(current_orientation) #[roll, pitch, yaw]


    def smooth_rise(self):
        inc = 0.05
        smooth = ModelState()
        for i in (0, self.takeoff.pose.position.z, inc):
            smooth.pose.position.z = i
            self.drone.publish(smooth)
            sleep(0.25)


    def main(self):
        while not rospy.is_shutdown():
            if self.takeoff_state == True:
                self.drone.publish(self.takeoff)

            if self.forward_state == True:
                self.drone.publish(self.takeoff)
                self.forward_state = False
            
            if self.backward_state == True:
                self.drone.publish(self.takeoff)
                self.backward_state = False
            
            if self.left_state == True:
                self.drone.publish(self.takeoff)
                self.left_state = False
            
            if self.right_state == True:
                self.drone.publish(self.takeoff)
                self.right_state = False

            if self.yaw_right_state == True:
                self.drone.publish(self.takeoff)
                self.yaw_right_state = False

            if self.yaw_left_state == True:
                self.drone.publish(self.takeoff)
                self.yaw_left_state = False
            
            print(self.current_euler)
            #print(self.target_quaternion)
            self.rate.sleep()
            #ent.unregister()

if __name__ == "__main__":
    sim = Drone(model, ref)
    sim.main()