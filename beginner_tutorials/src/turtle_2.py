#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/turtle_2.py
from initTurtle import initRobots
import math


class Turtle2(initRobots):


    def __init__(self,nodeId):
        self.nodeId = nodeId
        self.__clockTurn = -1
        self.__degree = 180
        self.__speed = 60
        self.__increaseRate = 0.6
        self.__tourCount = 6 # in 6 stop not continue

        super().__init__(nodeId)

        self.__moveRobot(60,180,0.60,-1,1)#60 constant, 180 for semi circle, 0.60 vertical speed, -1 clockwise, 1 for tour count 



    def __moveRobot(self,speed, angle, lspeed, clockwise,count):

        if count == self.__tourCount:
            self.stopRobot()
            return
            
        angular_speed = speed*(math.pi/180.0) 
        relativeangle = angle*(math.pi/180.0)
        
        self.vel.linear.x  = lspeed
        self.vel.angular.z = (angular_speed * clockwise)
        
        t0 = self.rospy.Time.now().to_sec() 
        current_angle = 0 
        
        
        while current_angle < relativeangle: 
            self.pub.publish(self.vel) 
            t1 = self.rospy.Time.now().to_sec() 
            current_angle = (t1 - t0) * angular_speed
            self.rate.sleep() 
        
        lspeed += self.__increaseRate
        count += 1
        self.__moveRobot(self.__speed, self.__degree, lspeed, self.__clockTurn, count)

    







       
     


            


