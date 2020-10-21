#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_arm', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=10)

# Display joint space paths and available trajectories.
group.set_named_target("top_mid")
group.go()
rospy.sleep(4)

group.set_named_target("top_left")
group.go()
rospy.sleep(4)

group.set_named_target("mid_left")
group.go()
rospy.sleep(4)

group.set_named_target("mid_mid")
group.go()
rospy.sleep(4)

group.set_named_target("bottom_left")
group.go()
rospy.sleep(4)

group.set_named_target("bottom_right")
group.go()
rospy.sleep(4)

group.set_named_target("mid_mid")
group.go()
rospy.sleep(4)

group.set_named_target("mid_right")
group.go()
rospy.sleep(4)

group.set_named_target("top_right")
group.go()
rospy.sleep(4)

group.set_named_target("allZeroes")
group.go()
rospy.sleep(4)


moveit_commander.roscpp_shutdown()