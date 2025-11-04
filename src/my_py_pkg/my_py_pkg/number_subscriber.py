import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberSubscriber(Node):
    def __init__(self):
        super().__init__("number_subscriber_node")
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        self.get_logger().info("Number Counter has been started.")

    def callback_number(self, msg: Int64):
        self.get_logger().info(f"I heard: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = NumberSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()