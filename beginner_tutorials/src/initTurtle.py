#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/initTurtle.py
import rospy
from geometry_msgs.msg import Twist

class initRobots:

    def __init__(self,nodeID):
        self.rospy = rospy
        self.nodeId = nodeID
        self.nodeName = "turtle" + self.nodeId
        
        self.rospy.init_node('movement',anonymous=True)
        self.pub = rospy.Publisher(self.nodeName + '/cmd_vel', Twist, queue_size=10)

        self.vel = Twist()
        self.__DEFAULT_LINEAR_VELOCITY = 0.3

        self.vel.linear.x  = self.__DEFAULT_LINEAR_VELOCITY
        self.vel.linear.y  = 0
        self.vel.linear.z  = 0
        self.vel.angular.x = 0
        self.vel.angular.y = 0
        self.vel.angular.z = 0

        self.rate = self.rospy.Rate(10)
        self.rospy.loginfo("Moving...")
          

    def stopRobot(self):  
        self.vel.linear.x = 0.0    
        self.vel.angular.z = 0.0
        self.pub.publish(self.vel) 
        self.rospy.loginfo("Stop")      









