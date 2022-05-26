#!/usr/bin/env python3
#18070006034 Nuri Can ÖZTÜRK

import rospy,sys
from beginner_msgsrv.srv import AddTwoInts, AddTwoIntsResponse



def add_two_ints_client(a1, b1):
    rospy.wait_for_service("add_two_ints")
    try:
            add_twoints= rospy.ServiceProxy("add_two_ints",AddTwoInts)
            response = add_twoints(a1, b1)
            response.sum

    except ServiceException:
        print("Error: ")
            

if __name__ == "__main__":
    a1 = int(sys.argv[1])
    b1 = int(sys.argv[2])
    print("Result: %s"%add_two_ints_client(a1,b1))
    #add_two_ints_server()     

