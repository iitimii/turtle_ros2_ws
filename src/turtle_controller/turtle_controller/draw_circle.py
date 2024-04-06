#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode_Class(Node):
    def __init__(self) -> None:
        super().__init__("Draw_Cricle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(0.5, self.send_velocity_cmd)
        self.get_logger().info("Draw Circle Node Started")

    def send_velocity_cmd(self):
        msg = Twist()
        msg.linear.x = 3.0
        msg.angular.z = 3.0
        self.cmd_vel_pub_.publish(msg)
        



def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode_Class()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()