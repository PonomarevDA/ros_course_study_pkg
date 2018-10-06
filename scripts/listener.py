#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64
from study_pkg.msg import Control

def callback(msg):
    rospy.loginfo("Received: steer = %d, speed = %d", msg.steer, msg.speed)

rospy.init_node('listener')
rospy.Subscriber('my_chat_topic', Control, callback)
rospy.spin()
