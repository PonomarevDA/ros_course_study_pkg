#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

rospy.init_node('listener')
rospy.Subscriber('my_chat_topic', Int64, callback)
rospy.spin()
