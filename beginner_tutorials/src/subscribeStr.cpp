#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>


using namespace std;


void callbackFunc(const std_msgs::String::ConstPtr& message)
{
    ROS_INFO("Received Message: %s",message->data.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc,argv,"stringSubscriber");
    ros::NodeHandle n;
    ros::Subscriber wordsub = n.subscribe<std_msgs::String>("/words",10,callbackFunc);
    ros::spin();
    return 0;
}