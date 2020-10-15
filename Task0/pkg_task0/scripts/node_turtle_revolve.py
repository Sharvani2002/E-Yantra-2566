#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

def pose_callback(msg):
    # print(msg.theta)
    print(msg.x)

def main():
	rospy.init_node('turtle_revolve', anonymous=True)

	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	vel_msg.linear.x=1
	vel_msg.linear.y=0
	vel_msg.linear.z=0
	vel_msg.angular.x=0
	vel_msg.angular.y=0
	vel_msg.angular.z=0.5

	pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
	pose_msg= Pose()
	pose_msg.x=0
	pose_msg.y=0
	distance = 12.56637061


	# while not rospy.is_shutdown():

	t0= rospy.Time.now().to_sec()
	current_distance= 0

	while(current_distance< distance):
		velocity_publisher.publish(vel_msg)
		t1=rospy.Time.now().to_sec()
		current_distance= sqrt(1)*(t1-t0)

	vel_msg.linear.x=0
	vel_msg.linear.y=0
	vel_msg.angular.z=0
	velocity_publisher.publish(vel_msg)

	print(vel_msg)




if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

