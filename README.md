# AlMahirROSDrone

This is a ROS package created by me

Help regarding the URDF model was taken from Dagothar (https://deltastep.blogspot.com/2020/01/simulating-drone-in-gazebo.html) 

This is a quadroter that has the plugin made in python cause my C++ is horrible so I went the python route to make the whole thing move.

Definitely has a lot of flaws, hoping to work more on it or work on something else completely relating to it.

I made this on Ubuntu 20.04 (ROS Noetic).

After compiling everything you can run 

<code> roslaunch almahir_drone gazebo.launch </code>

Doing this will launch a gazebo simulation as well as the python plugin. There is a controller node in the source that uses pygame to control the drone. 

To run the controller node:

<code> rosrun almahir_drone drone_controller.py </code> 

Feedback is appreciated, thank you
