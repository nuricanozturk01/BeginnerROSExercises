#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/midterm.py


from contextlib import nullcontext
from dis import dis
from math import dist
from shutil import move
from turtle import speed
from turtlesim.msg import Pose
import rospy
import sys
from geometry_msgs.msg import Twist

nodeId = str(sys.argv[1])
nodeName = "turtle" + nodeId

class initRobots:

    def __init__(self,x=0.3):
        rospy.init_node('move',anonymous=True)
        self.pub = rospy.Publisher(nodeName+'/cmd_vel',Twist,queue_size=10)
        
        self.vel = Twist()

        self.vel.linear.x  = x
        
        self.vel.linear.y  = 0
        self.vel.linear.z  = 0
        self.vel.angular.x = 0
        self.vel.angular.y = 0
        self.vel.angular.z = 0
        self.rate = rospy.Rate(10)
        rospy.loginfo("Moving...")

    def getPub(self):
        return self.pub
    def getVel(self):
        return self.vel
    def getRate(self):
        return self.rate             

    

class Turtle1(initRobots):

    def __init__(self):
        super().__init__()
        self.distance = 1
        print(type(self.vel.angular.z))
        #exit()
        
    def turn(self,count):
        self.vel.linear.x = 0
        self.vel.linear.y = 0
        self.vel.angular.z = -0.4
        time = 1.52
        currentDistance = 0
        t0 = rospy.Time.now().to_sec() #current time
        time *= count 
        while currentDistance < time:
            self.pub.publish(self.vel)
            t1 = rospy.Time.now().to_sec() #get current time
            currentDistance = (t1 - t0) * abs(self.vel.angular.z)
            print(currentDistance)  
            self.rate.sleep()  

        self.stopRobot()     
        #exit()    


    def goBelow(self,distance):
            self.turn(1)
            self.vel.linear.x = 0.3
            self.vel.linear.y = 0           

            currentDistance = 0
            t0 = rospy.Time.now().to_sec() #current time
            while currentDistance < distance: # not is_shutdown ctrl+c veya ctrl_z yapana kadar devam eder
                self.pub.publish(self.vel) # publish velocity message
                t1 = rospy.Time.now().to_sec() #get current time
                currentDistance = (t1 - t0) * abs(self.vel.linear.x)
                self.rate.sleep()   

    def go(self,distance,speed):
        
       t0 = rospy.Time.now().to_sec() #current time
       currentDistance = 0
       self.vel.linear.x = speed
       self.vel.linear.y = 0 

       while currentDistance < distance:
            self.pub.publish(self.vel)            
            t1 = rospy.Time.now().to_sec() 
            currentDistance = (t1 - t0) * abs(self.vel.linear.x )
            self.rate.sleep()

    def startTour(self,firstTourFlag,secondTourFlag,isFirst):
        
        if isFirst:
            self.go(self.distance,0.3)
            self.goBelow(0.3)
            self.turn(1)
            self.go(self.distance,+0.3)
        else:
            if firstTourFlag == secondTourFlag:
                self.distance += 1
                self.goBelow(0.3)
                self.go(self.distance,0.3)
                self.goBelow(0.3)
                self.go(self.distance,-0.3)
            if firstTourFlag != secondTourFlag:
               self.distance *= 2
               self.go(self.distance,-0.3)
               self.goBelow(0.3)
               self.go(self.distance,0.3)

    # True => Right     -   False=> Left   
    def move(self):
        
        
        self.startTour(True,True,True) # first tour second parameter false

        self.startTour(True,True,False)
        self.startTour(True,False,False)
        
    def stopRobot(self):
        #Stop the robot    
        self.vel.linear.x = 0.0 
        self.vel.linear.y = 0.0    
        self.vel.angular.z = 0.0
        self.pub.publish(self.vel) 
        rospy.loginfo("Stop")  



class Turtle2:
    def __init__(self):
        print("NO!")




if __name__ == "__main__":
    try:

        turtle = nullcontext
        if nodeId == "1":
            turtle = Turtle1()
            turtle.move()

        
    except rospy.ROSInterruptException:
        pass        