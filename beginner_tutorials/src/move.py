#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/move.py
# Remind: remapping
import rospy,sys
from geometry_msgs.msg import Twist
nodeId = str(sys.argv[1])
nodeName = "robot_" + nodeId
def moveRobot():
    #rospy.init_node('move')
    #pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10) # turtlesim 1 turtle
    rospy.init_node(nodeName,anonymous=True)
    #pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10) # stage 1 robot
    pub = rospy.Publisher(nodeName+'/cmd_vel',Twist,queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x  = 0.2
    vel_msg.linear.y  = 0
    vel_msg.linear.z  = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

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