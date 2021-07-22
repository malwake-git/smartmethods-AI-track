#!/usr/bin/env python

import rospy
from std_msgs.msg import Header
import rospy
from geometry_msgs.msg import PoseStamped

rospy.init_node("mynode")

goal_publisher = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=5)

goal = PoseStamped()

goal.header.seq = 1
goal.header.stamp = rospy.Time.now()
goal.header.frame_id = "map"

goal.pose.position.x = 1.0
goal.pose.position.y = 2.0
goal.pose.position.z = 0.0

goal.pose.orientation.x = 0.0
goal.pose.orientation.y = 0.0
goal.pose.orientation.z = 0.0
goal.pose.orientation.w = 1.0

rospy.sleep(1)
goal_publisher.publish(goal)

rospy.spin()
