#!/usr/bin/env python3
#18070006034 Nuri Can ÖZTÜRK

import rospy
from beginner_msgsrv.srv import AddTwoInts, AddTwoIntsResponse


def handle_adding_two_ints(req):
    print("Adding the numbers. %s"%(req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)
def add_two_ints_server():
    rospy.init_node("add_two_ints_server")
    rospy.Service("add_two_ints",AddTwoInts,handle_adding_two_ints)
    print("Start services")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()        
