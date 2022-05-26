#!/usr/bin/env python
#18070006034 Nuri Can ÖZTÜRK
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/main.py

import sys,rospy
from turtle_1 import Turtle1
from turtle_2 import Turtle2

nodeId = str(sys.argv[1])

if __name__ == "__main__":
    try:
        Turtle1(nodeId) if nodeId == "1" else Turtle2(nodeId)    
    except rospy.ROSInterruptException:    
        pass