#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#18070006034 Nuri Can ÖZTÜRK

import rospy,sys
from euclideanDistance.srv import EuclideanDistance, EuclideanDistanceResponse



def steering_angle_client(goal_pose_y, odom_y, goal_pose_x, odom_x):
    rospy.wait_for_service("euclideanDistanceServer")
    try:
            calculateSteeringAngle= rospy.ServiceProxy("euclideanDistanceServer",EuclideanDistance)
            response = calculateSteeringAngle(goal_pose_y, odom_y, goal_pose_x, odom_x)
            return response.result

    except Exception:
        print("Error: ")
            

if __name__ == "__main__":
    goal_pose_y = float(sys.argv[1])
    odom_y = float(sys.argv[2])
    goal_pose_x = float(sys.argv[3])
    odom_x = float(sys.argv[4])
    print(steering_angle_client(goal_pose_y, odom_y, goal_pose_x, odom_x))
  

