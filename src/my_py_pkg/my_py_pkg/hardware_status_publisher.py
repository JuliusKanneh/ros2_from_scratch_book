import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwareStatusPublisher(Node):
    def __init__(self):
        super().__init__("hardware_status_publisher_node")
        self.hardware_status_publisher_ = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self.hardware_status_timer_ = self.create_timer(5.0, self.publish_hardware_status)
        self.get_logger().info("Hardware status publisher has started.")

    def publish_hardware_status(self):
        status_msg = HardwareStatus()
        status_msg.version = 1
        status_msg.temperature = 36.5
        status_msg.are_motors_ready = True
        status_msg.debug_message = "All systems operational."
        self.hardware_status_publisher_.publish(msg=status_msg)
        self.get_logger().info(f"Published Hardware Status: Version: {status_msg.version}, Temperature: {status_msg.temperature}, Motors Ready: {status_msg.are_motors_ready}, Debug: {status_msg.debug_message}")

def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()