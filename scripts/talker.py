#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64
from study_pkg.msg import Control

rospy.init_node('talker')
pub = rospy.Publisher('my_chat_topic', Control, queue_size=10)
rate = rospy.Rate(10)

def start_talker():
    msg = Control()
    msg.steer = 40
    msg.speed = 1
    while not rospy.is_shutdown():
        msg.steer += 1
        rospy.loginfo(str(msg.steer) + ' ' + str(msg.speed)) # output to terminal
        pub.publish(msg)        # publish to topic
        rate.sleep()            # sleep rate^(-1) second's

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
