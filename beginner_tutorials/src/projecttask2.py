#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/moveToGo.py

import rospy
from geometry_msgs.msg import Twist,Point
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
from math import atan2, pow,sqrt
import sys
from tf.transformations import euler_from_quaternion
from euclideanDistance.srv import EuclideanDistance, EuclideanDistanceResponse



class Turtlebot:


    def __init__(self,nodeName,goalx,goaly):
        rospy.init_node("name",anonymous=True)
        self.pub = rospy.Publisher(nodeName + '/cmd_vel',Twist,queue_size=100)
        self.sub = rospy.Subscriber(nodeName+"/odom",Odometry,callback=self.update_pose)
        self.odometry = Odometry()
        self.rate = rospy.Rate(10)
        self.goalX = goalx
        self.goalY = goaly
        

    def update_pose(self,msg):
        self.odometry = msg
        self.orientation_q = msg.pose.pose.orientation
        self.orientation_list = [self.orientation_q.x, self.orientation_q.y, self.orientation_q.z, self.orientation_q.w]
        (self.roll, self.pitch, self.yaw) = euler_from_quaternion (self.orientation_list)

    def euclidean_distance(self,goal_pose):    
       #return sqrt(pow((goal_pose.x - self.odometry.pose.pose.position.x),2) + pow((goal_pose.y - self.odometry.pose.pose.position.y),2))
	rospy.wait_for_service("euclideanDistanceServer")
   	try:
            calculateSteeringAngle= rospy.ServiceProxy("euclideanDistanceServer",EuclideanDistance)
            response = calculateSteeringAngle(goal_pose.y, self.odometry.pose.pose.position.y, goal_pose.x, self.odometry.pose.pose.position.x)
            rospy.loginfo(response.result)
	    return response.result
	  

    	except Exception:
       	  print("Error: ")  
		  

    def linear_vel(self,goal_pose,constant=1.5):
        return constant * self.euclidean_distance(goal_pose)  

    def steering_angle(self,goal_pose):
        return atan2(goal_pose.y - self.odometry.pose.pose.position.y, goal_pose.x - self.odometry.pose.pose.position.x)

    def angular_vel(self,goal_pose,constant=6):
        return constant * (self.steering_angle(goal_pose) - goal_pose.theta)

    def move2goal (self):
        goalpose = Pose()
    
        goalpose.x = self.goalX
        goalpose.y = self.goalY
        
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
            self.rate.sleep()
		
            
        vel_msg.linear.x  = 0
        vel_msg.angular.z = 0
        self.pub.publish(vel_msg)
        rospy.spin()


def main(nodeName):
	if nodeName == "robot_0":
		x = Turtlebot(nodeName,1,0)
		x.move2goal()   
		rospy.spin()
        else:
	    x = Turtlebot(nodeName,5,0)
	    x.move2goal()   
	    rospy.spin()

if __name__ == "__main__":
    nodeId = str(sys.argv[1])
    nodeName = "robot_"+nodeId 
    	
    try:
	goalx = int(sys.argv[2])
	goaly = int(sys.argv[3])

        x = Turtlebot(nodeName,goalx,goaly)
        x.move2goal()   
	rospy.spin()
               
    except IndexError:	
	main(nodeName)
    except Exception:
	main(nodeName)
    except rospy.ROSInterruptException:
        pass
	   	
