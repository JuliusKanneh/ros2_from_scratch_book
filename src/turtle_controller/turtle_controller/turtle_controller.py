import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time

class TurtleController(Node):
    def __init__(self):
        super().__init__("turtle_controller_node")
        self.get_logger().info("Turtle Controller Node has started.")
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.cmd_vel_subscription = self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 10)

    def pose_callback(self, msg: Pose):
        self.get_logger().info("Drawing Circle based on Turtle Pose...")
        self.get_logger().info(f"Turtle Pose - x: {msg.x}, y: {msg.y}, theta: {msg.theta}")
        turtle_pose_msg = Twist()
        if msg.x < 5.5:
            turtle_pose_msg.linear.x = 1.0
            turtle_pose_msg.angular.z = 1.0
        else:
            turtle_pose_msg.linear.x = 2.0
            turtle_pose_msg.angular.z = 2.0

        self.cmd_vel_publisher_.publish(turtle_pose_msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()