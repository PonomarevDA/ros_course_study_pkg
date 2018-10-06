#include <ros/ros.h>
#include <std_msgs/String.h>
#include <study_pkg/Control.h>

void topicCallback(const study_pkg::Control::ConstPtr& msg)
{
  ROS_INFO("Speed: %d / Steer: %d", msg->speed, msg->steer);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("cpp_chatter", 1000, topicCallback);

  ros::spin();

  return 0;
}
