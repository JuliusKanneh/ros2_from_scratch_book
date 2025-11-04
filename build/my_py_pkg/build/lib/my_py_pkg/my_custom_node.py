import rclpy
from rclpy.node import Node

class MyCustomNode(Node):
    def __init__(self):
        super().__init__('my_custom_node')
        self._counter = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(f'Counter: {self._counter}')
        self._counter += 1

def main(args=None):
        rclpy.init(args=args)
        node = MyCustomNode()
        rclpy.spin(node)
        rclpy.shutdown()

if __name__ == "__main__":
    main()