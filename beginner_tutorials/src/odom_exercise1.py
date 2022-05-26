#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/moveToGo.py
import rospy,sys
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

# rosmsg show nav_msgs/Odometry

#nodeId = str(sys.argv[1])
#nodeName = "tb3_"+nodeId
def callback(msg):
    print (msg.pose.pose)

def moveTask():
    pub = rospy.Publisher("robot_0/cmd_vel",Twist,queue_size=10) #stage
    #pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10) #gazebo 1 robot
    #pub = rospy.Publisher(nodeName+"/cmd_vel",Twist,queue_size=10) #gazebo 1 robot
    vel_msg = Twist()
    vel_msg.linear.x  = 0.5
    vel_msg.linear.y  = 0
    vel_msg.linear.z  = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.2

    while not rospy.is_shutdown():
        pub.publish(vel_msg)

    vel_msg.linear.x  = 0
    vel_msg.angular.z  = 0
    pub.publish(vel_msg)
rospy.init_node("asd",anonymous=True)
odom_sub = rospy.Subscriber("robot_0/odom",Odometry,callback=callback) #robot_0 ın pozisyonu için robot_0 koyduk    (Stage)
# robotun konumu (1,2) bile olsa robot (1,2) noktasını (0,0) kabul eder ve bize ona göre bilgi verir    
#odom_sub = rospy.Subscriber("/odom",Odometry,callback=callback) # one robot
#odom_sub = rospy.Subscriber(nodeName+"/odom",Odometry,callback=callback) # one robot

moveTask()
rospy.spin()    

