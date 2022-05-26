#include "ros/ros.h"
#include "gazebo_msgs/SetModelState.h"
#include <std_srvs/Empty.h>

using namespace std;

ros::Publisher Velocity_publisher;
geometry_msgs::Twist Cmd;
const float TURN_WAIT_TIME_SECONDS = 0.5;
void forward(float dist);

int main(int argc, char **argv)
{
	ros::init(argc,argv,"gazebocontrol1");
	ROS_INFO("Lets start");
	ros::NodeHandle n;
	Velocity_publisher = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
	
	int i = 0;
	while(i < 5)
	{
		forward(0.2);
		ros::Duration(TURN_WAIT_TIME_SECONDS).sleep();
		++i;
		
	}
	
	 ros::ServiceClient clearClient = n.serviceClient<std_srvs::Empty>("/gazebo/reset_world");
    	 std_srvs::Empty srv;
    	 clearClient.call(srv);
}


void forward(float lv)
{
	Cmd.linear.x = lv;
	Cmd.linear.y = 0;
	Cmd.linear.y = 0;
	Cmd.angular.x = 0;
	Cmd.angular.y = 0;
	Cmd.angular.z = 0;
	Velocity_publisher.publish(Cmd);
}
