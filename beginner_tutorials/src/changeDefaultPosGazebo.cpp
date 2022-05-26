#include "ros/ros.h"
#include "gazebo_msgs/SetModelState.h"
#include "gazebo_msgs/ModelStates.h"


using namespace std;
ros::Publisher Velocity_publisher;
geometry_msgs::Twist Cmd;
const float TURN_WAIT_TIME_SECONDS = 0.5;

int main(int argc, char **argv)
{
	ros::init(argc, argv, "gazebocontrol1");
	ROS_INFO("Lets start");
	ros::NodeHandle n;
	ros::service::waitForService("/gazebo/set_model_state");
	ros::ServiceClient client = n.serviceClient<gazebo_msgs::SetModelState>("/gazebo/set_model_state");
	
	geometry_msgs::Point turtle_position;
	turtle_position.x = 1;
	turtle_position.y = 1;
	turtle_position.z = 0;
	
	geometry_msgs::Quaternion turtle_orientation;
	turtle_orientation.x = 0;
	turtle_orientation.y = 0;
	turtle_orientation.z = 0;
	turtle_orientation.w = 0;
	
	geometry_msgs::Pose turtle_pose;
	turtle_pose.position = turtle_position;
	turtle_pose.orientation = turtle_orientation;	
	
	gazebo_msgs::ModelState modelState;
	modelState.model_name = "turtlebot3_burger";
	modelState.reference_frame = "world"; //tf tree
	modelState.pose = turtle_pose;
	
	gazebo_msgs::SetModelState setModelState;
	setModelState.request.model_state = modelState;
	client.call(setModelState);
	
}
