#!/usr/bin/env python3

import rclpy
from rclpy.node import Node



class MyNode(Node):

    def __init__(self):
        super().__init__("First_Node_name")
        self.get_logger().info("Created Node Timi098")
        self.create_timer(0.00001, self.timer_callback)
        print("Hello")
        self.counter = 0

    def timer_callback(self):
        self.get_logger().info(f"Lol {self.counter}")
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()



if __name__ == '__main__':
    main()