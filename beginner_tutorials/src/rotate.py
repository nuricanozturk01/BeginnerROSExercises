#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/rotate.py

from turtle import speed
import math
import rospy
import sys
from geometry_msgs.msg import Twist

nodeId = str(sys.argv[1])
nodeName = "turtle" + nodeId

rospy.init_node(nodeName,anonymous=True)
#pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
pub = rospy.Publisher(nodeName + '/cmd_vel',Twist,queue_size=10)
vel_msg = Twist()
vel_msg.linear.x  = 0
vel_msg.linear.y  = 0
vel_msg.linear.z  = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0



def moveRobot(speed, angle, lspeed, clockwise):

    angular_speed = speed*(math.pi/180.0) 
    relativeangle = angle*(math.pi/180.0)
    vel_msg.linear.x  = lspeed
    vel_msg.angular.z = angular_speed * clockwise
    
    rate = rospy.Rate(10)
    rospy.loginfo("Moving...")

    #distance = 2.0 # The distance that we wish to travel
    t0 = rospy.Time.now().to_sec() #current time
    current_angle = 0 # will be updated in the while loop
    
    
    while current_angle < relativeangle: # not is_shutdown ctrl+c veya ctrl_z yapana kadar devam eder
        pub.publish(vel_msg) # publish velocity message
        t1 = rospy.Time.now().to_sec() #get current time
        current_angle = (t1 - t0) * angular_speed
        # current_angle = (t1 - t0) * vel_msg.linear.z #if it is clockwise 
        rate.sleep() 

    #Stop the robot    
    vel_msg.linear.x = 0.0    
    vel_msg.angular.z = 0.0
    pub.publish(vel_msg) 
    

if __name__  == "__main__":
    try:

        moveRobot(10,90,0.7,1) if nodeId == "1" else moveRobot(5,60,0.2,-1)
        #if nodeId == "1":
           # moveRobot(10,90,0.7,1)
        #else : moveRobot(5,60,0.2,-1)
    except rospy.ROSInterruptException:
        pass        