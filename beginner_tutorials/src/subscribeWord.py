#!/usr/bin/env python

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/subscribeWord.py
#18070006034 Nuri Can ÖZTÜRK
import rospy
from std_msgs.msg import String

rospy.init_node('stringSub') # you can give any node name

def callbackfun(msg): # msg parameter must be include msg
    print(msg)
sub = rospy.Subscriber('/words',String,callback=callbackfun)# topicname must be same with server


rospy.spin()

