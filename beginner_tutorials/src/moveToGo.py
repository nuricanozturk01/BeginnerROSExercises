#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/moveToGo.py

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, pow,sqrt
import sys

a_x = int(sys.argv[1])
nodeId = str(sys.argv[2])
nodeName = "robot_" + nodeId

class Turtlebot:


    def __init__(self,x):
        rospy.init_node("turtlenode",anonymous=True)
        self.x = x
        self.pub = rospy.Publisher(nodeName + '/cmd_vel',Twist,queue_size=10)
        self.sub = rospy.Subscriber(nodeName+"/pose",Pose,callback=self.update_pose) # loop
        self.pose = Pose()
        self.pose.x = 4
        self.pose.y = 4
        rate = rospy.Rate(10)

    def update_pose(self,data):
        self.pose = data

    def euclidean_distance(self,goal_pose):    
       return sqrt(pow((goal_pose.x - self.pose.x),2) + pow((goal_pose.y - self.pose.y),2))
    
    def linear_vel(self,goal_pose,constant=1.5):
        return constant * self.euclidean_distance(goal_pose)  

    def steering_angle(self,goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self,goal_pose,constant=6):
        return constant * (self.steering_angle(goal_pose ) - self.pose.theta)

    def move2goal (self):
        goalpose = Pose()
    
        goalpose.x = self.x
        goalpose.y = 1

        tolarence = 0.01
        vel_msg = Twist()
    
        while self.euclidean_distance(goalpose)>= tolarence:
            vel_msg.linear.x  = self.linear_vel(goalpose)
            vel_msg.linear.y  = 0
            vel_msg.linear.z  = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goalpose)
            self.pub.publish(vel_msg)
            
        vel_msg.linear.x  = 0
        vel_msg.angular.z = 0
        self.pub.publish(vel_msg)     


if __name__ == "__main__":
    try:
        if nodeId == "1":   
            x = Turtlebot(a_x)
            x.move2goal()        
        else:
             x = Turtlebot(6)
             x.move2goal()           
    except rospy.ROSInterruptException:
        pass       
