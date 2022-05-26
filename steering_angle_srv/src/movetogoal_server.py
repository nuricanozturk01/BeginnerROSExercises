#!/usr/bin/env python3
#18070006034 Nuri Can ÖZTÜRK

import rospy
from math import atan2
from steering_angle_srv.srv import SteeringAngle, SteeringAngleResponse


def handle_steering_angle(req):
    result = atan2((req.goal_pose_y - req.pose_y),(req.goal_pose_x - req.pose_x))
    print(result)
    print("Result is %s"%result)
    return SteeringAngleResponse(result)
def steering_angle_server():
    rospy.init_node("steering_angle_server")
    rospy.Service("steering_angle",SteeringAngle,handle_steering_angle)
    print("Start services")
    rospy.spin()

if __name__ == "__main__":
    steering_angle_server()        
