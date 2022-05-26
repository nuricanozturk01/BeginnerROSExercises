#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <nav_msgs/Odometry.h>

ros::Publisher pub;
geometry_msgs::Twist msg;

void callback(const nav_msgs::Odometry::ConstPtr &msg)
{
	ROS_INFO("%s", msg->header.frame_id.c_str());
	ROS_INFO("%f", msg->twist.twist.linear.x);
	ROS_INFO("%f", msg->pose.pose.position.x);
}

void move(ros::NodeHandle n)
{
	pub = n.advertise<geometry_msgs::Twist>("robot_0/cmd_vel", 1000);
	ros::Rate loop_rate(10);

	while(ros::ok())	
	{
		msg.linear.x = 0.2;
		pub.publish(msg);
		ros::spinOnce();
		loop_rate.sleep();
	}
}

int main(int argc, char **argv)
{
	ros::init(argc,argv,"odomnode");
	ros::NodeHandle n;
	ros::Subscriber sub = n.subscribe("robot_0/odom",1000,callback);
	move(n);
	ros::spin();

	return 0;
}



