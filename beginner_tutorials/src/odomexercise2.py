#!/usr/bin/env python3
#18070006034 Nuri Can ÖZTÜRK

import rospy,sys
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry





vel_msg = Twist()
vel_msg.linear.x  = 0
vel_msg.linear.y  = 0
vel_msg.linear.z  = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0

def callback(msg):
    rospy.loginfo(msg.pose.pose)



def move():
    
    pub = rospy.Publisher("robot_0/cmd_vel",Twist,queue_size=10) #stage
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():        
        vel_msg.linear.x = 0.2
        pub.publish(vel_msg)
        rate.sleep()
    rospy.spin()

rospy.init_node("stage",anonymous=True)
odom_sub = rospy.Subscriber("robot_0/odom",Odometry,callback=callback)
move()
rospy.spin()
