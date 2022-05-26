#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class InitStage:
    def __init__(self, nodeID):


        self.nodeID = nodeID
        self.rospy = rospy
        self.nodeName = "robot_0" + self.nodeID

        self.rospy.init_node(self.nodeName,anonymous=True) 
        self.pub = rospy.Publisher(self.nodeName + '/cmd_vel', Twist, queue_size=10)
        
        self.vel_msg = Twist()
        
        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.rate = self.rospy.Rate(10)

        self.MIN_FRONT_DIST=0.9
        self.STOP_DIST = 0.7

        self.STOP = 0
        self.OBSTACLE = False
        self.SPEED = 0.5
        self.SSPEED = 0.1
        self.MIN_LEFT=1000000.0
        self.MIN_RIGHT=1000000.0

        self.MAX_LEFT = -1
        self.MAX_RIGHT = -1
    
    
    def stopRobot(self):  
        self.vel_msg.linear.x = 0.0    
        self.vel_msg.angular.z = 0.0
        self.pub.publish(self.vel_msg) 
        self.rospy.loginfo("Stop")        
