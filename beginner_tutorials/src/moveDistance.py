#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/moveDistance.py
# Remind: remapping

from turtle import speed
import rospy
import sys
from geometry_msgs.msg import Twist

#nodeId = str(sys.argv[1])
#nodeName = "turtle" + nodeId

def moveRobot():
    rospy.init_node('move')
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x  = 0.1
    vel_msg.linear.y  = 0
    vel_msg.linear.z  = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    rate = rospy.Rate(10)
    rospy.loginfo("Moving...")

    distance = 2.0 # The distance that we wish to travel
    t0 = rospy.Time.now().to_sec() #current time
    currentDistance = 0 # will be updated in the while loop
    
    
    while currentDistance < distance: # not is_shutdown ctrl+c veya ctrl_z yapana kadar devam eder
        pub.publish(vel_msg) # publish velocity message
        t1 = rospy.Time.now().to_sec() #get current time
        currentDistance = (t1 - t0) * vel_msg.linear.x 
        rate.sleep() 

    #Stop the robot    
    vel_msg.linear.x = 0.0    
    vel_msg.angular.z = 0.0
    pub.publish(vel_msg) 
    rospy.loginfo("Stop")

if __name__  == "__main__":
    try:
        moveRobot()
    except rospy.ROSInterruptException:
        pass        