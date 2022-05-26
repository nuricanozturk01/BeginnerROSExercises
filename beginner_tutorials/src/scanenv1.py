#!/usr/bin/env python
#18070006039 Umut Emre Celik
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/scanenv1.py

import rospy
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

nodeId = str(sys.argv[1])
nodeName = "robot_" + nodeId

vel_msg = Twist()
vel_msg.linear.x = 0.5
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0

def callback(msg):
	#for i in range((0,len(msg.ranges))):
	#	print(str(msg.ranges[i]))
		
	for i in msg.ranges:
		print (str(i))
		

		
	obstacle = False	
	#print('s[0]: '+ str(msg.ranges[0]) +
	#	  's[90]: '+ str(msg.ranges[90])+
	#	  's[135]: '+ str(msg.ranges[135]))
	#msg.ranges[135] > 0.5

	for i in range(len(msg.ranges)):
		if (i >= 0 and i <= 35) or (i >= 125 and i <= 142) or (i >= 235 and i <= 260):
				if msg.ranges[i] < 0.5:
					obstacle = True
			
		


	# 0 -35  125-142  235-260
	#if (msg.ranges[i] > 0.5):
	if (not(obstacle)):
		vel_msg.linear.x = 0.5
		vel_msg.linear.y = 0.0
	else:
		vel_msg.linear.x = 0.0
		vel_msg.linear.y = 0.0

	pub.publish(vel_msg)


rospy.init_node(nodeName , anonymous = True)
pub = rospy.Publisher(nodeName + '/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber(nodeName+'/base_scan', LaserScan , callback)# scan => for Gazebo
rospy.spin()