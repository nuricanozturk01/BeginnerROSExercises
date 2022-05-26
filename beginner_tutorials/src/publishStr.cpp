#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>


using namespace std;

int main(int argc, char **argv)
{
    ros::init(argc,argv,"stringPublisher");
    ros::NodeHandle n;
    ros::Publisher wordpub = n.advertise<std_msgs::String>("/words",10);
    ros::Rate myRate(10);
    int count = 0;

    while(ros::ok())
    {
        std_msgs::String message;
        stringstream ss;
        ss<<"Hello "<<count;
        message.data = ss.str();
        ROS_INFO("%s",message.data.c_str());
        wordpub.publish(message);
        myRate.sleep();
        count++;
    }
    return 0;
}