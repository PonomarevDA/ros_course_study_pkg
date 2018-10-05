#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64

rospy.init_node('talker')
pub = rospy.Publisher('my_chat_topic', Int64, queue_size=10)
rate = rospy.Rate(10)

def start_talker():
    msg = Int64()
    msg.data = 0
    while not rospy.is_shutdown():
        msg.data += 2
        rospy.loginfo(msg.data) # output to terminal
        pub.publish(msg)        # publish to topic
        rate.sleep()            # sleep rate^(-1) second's

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
