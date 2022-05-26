#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/publishWord.py

import rospy
from std_msgs.msg import String

rospy.init_node('stringpub')
pub = rospy.Publisher('/words',String,queue_size=10)
# /words topicName, String-> msg_type queue_size -> limit
msg = "Hello ROS!"
rate = rospy.Rate(10) # sleep

while not rospy.is_shutdown(): # not is_shutdown ctrl+c veya ctrl_z yapana kadar devam eder
    print(msg)
    pub.publish(msg)
    rate.sleep()
    
