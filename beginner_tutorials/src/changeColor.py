#!/usr/bin/env python3
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/changeColor.py

import rospy
from std_srvs.srv import Empty # call'İn
from turtlesim.srv import *


rospy.init_node('colorr',anonymous=True)

color_r = rospy.get_param('r')
color_g = rospy.get_param('g')
color_b = rospy.get_param('b')



print(color_r,color_g,color_b)
rospy.wait_for_service("clear")  #active clear service

rospy.set_param("background_r",color_r)
rospy.set_param("background_g",color_g)
rospy.set_param("background_b",color_b)

clear_background = rospy.ServiceProxy("/clear",Empty) # service_name , service_type
clear_background()

