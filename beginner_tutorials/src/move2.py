#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/move2.py
# Remind: remapping
import rospy
from geometry_msgs.msg import Twist

def moveRobot():
    rospy.init_node('move',anonymous=True)
    pub = rospy.Publisher('/turtle2/cmd_vel',Twist,queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x  = 0.3
    vel_msg.linear.y  = 0
    vel_msg.linear.z  = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.0

    rate = rospy.Rate(10) # sleep
    while not rospy.is_shutdown(): # not is_shutdown ctrl+c veya ctrl_z yapana kadar devam eder
        #print(msg)
        pub.publish(vel_msg)
        rate.sleep()

if __name__  == "__main__":
    try:
        moveRobot()
    except rospy.ROSInterruptException:
        pass    
