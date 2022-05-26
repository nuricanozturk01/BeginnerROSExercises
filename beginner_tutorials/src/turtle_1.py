#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/turtle_1.py
from initTurtle import initRobots

class Turtle1(initRobots):

    def __init__(self,nodeId):
        self.nodeId = nodeId
        self.__velocity = 0.3
        
        self.__downDistance = 0.2
        self.__distance = 1

        super().__init__(nodeId)
        self.__move() #init
                        

    def __go(self,lx,ly,lz,distance):

        self.vel.linear.x = lx
        self.vel.linear.y = ly
        self.vel.angular.z = lz

        vel = abs(lx) if lx != 0 else abs(ly)

        t0 = self.rospy.Time.now().to_sec()

        currentDistance = 0.0

        while currentDistance < distance:     
            self.pub.publish(self.vel)
            t1 = self.rospy.Time.now().to_sec() #get current time
            currentDistance = (t1 - t0) * abs(vel)
            self.rate.sleep()
       

    def __tour(self,prevD,currentD,first=False):
        
        if prevD == currentD and not first:
            self.__distance += 1
            self.__go(0, -self.__velocity , 0 , self.__downDistance)

        if (prevD != currentD):
            self.__distance *= 2
            self.__go(-self.__velocity,0,0,self.__distance)      
        
        else:
            self.__go(self.__velocity,0,0,self.__distance)  

        vel = self.vel.linear.x    
        self.__go(0, -self.__velocity , 0 , self.__downDistance)
        self.__go(-vel,0,0,self.__distance)

        
    def __move(self):
        self.__tour(True,True,True)
        self.__tour(True,True)
        self.__tour(True,False)
        self.stopRobot()     


        


        

