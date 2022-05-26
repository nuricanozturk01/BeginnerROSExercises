#!/usr/bin/env python3
#18070006034 Nuri Can ÖZTÜRK

import rospy,sys
from steering_angle_srv.srv import SteeringAngle, SteeringAngleResponse



def steering_angle_client(goal_y, pose_y, goal_x, pose_x):
    rospy.wait_for_service("steering_angle")
    try:
            calculateSteeringAngle= rospy.ServiceProxy("steering_angle",SteeringAngle)
            response = calculateSteeringAngle(goal_y, pose_y, goal_x, pose_x)
            return response

    except Exception:
        print("Error: ")
            

if __name__ == "__main__":
    goal_y = float(sys.argv[1])
    pose_y = float(sys.argv[2])
    goal_x = float(sys.argv[3])
    pose_x = float(sys.argv[4])
    print(steering_angle_client(goal_y, pose_y, goal_x, pose_x))
  

