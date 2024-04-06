#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class ClosedLoopControl(Node):
    def __init__(self):
        super().__init__("Pose_Velocity_Control")
        self.sub = self.create_subscription(Pose, "/turtle1/pose", self.publish_velocity, 10)
        self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        self.get_logger("Closed Loop Control is ON!")

    def publish_velocity(self):
        msg = Twist
        msg.angular = 3.0
        msg.linear = 3.0
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = ClosedLoopControl()
    rclpy.spin(node)
    rclpy.shutdown()