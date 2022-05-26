#include <ros/ros.h>
#include <std_srvs/Empty.h>
#include <turtlesim/Spawn.h>

int main(int argc, char **argv)
{
    ros::init(argc,argv,"setcolor");
    ros::NodeHandle n;
    int r,g,b;
    n.getParam("r",r);
    n.getParam("g",g);
    n.getParam("b",b);

    ros::service::waitForService("clear");
    ros::param::set("background_r",r);
    ros::param::set("background_g",g);
    ros::param::set("background_b",b);

    ros::ServiceClient clearClient = n.serviceClient<std_srvs::Empty>("clear");
    std_srvs::Empty srv;
    clearClient.call(srv);
    return 0;
}