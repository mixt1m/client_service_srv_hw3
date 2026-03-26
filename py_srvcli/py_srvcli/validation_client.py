import sys

from string_validation_interfaces.srv import Str
import rclpy
from rclpy.node import Node

class ValidationClient(Node):
    def __init__(self):
        super().__init__("validation_client")
        self.cli = self.create_client(Str, 'string_validation')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Str.Request()

    def send_request(self, text):
        self.req.str = text
        return self.cli.call_async(self.req)
    

def main():
    rclpy.init()

    validation_client = ValidationClient()

    text_to_validate = ' '.join(sys.argv[1:]) 
    
    future = validation_client.send_request(text_to_validate)
    rclpy.spin_until_future_complete(validation_client, future)
    
    response = future.result()

    validation_client.get_logger().info(
        'Validation result for "%s": %s' %
        (text_to_validate, response.is_valid)
    )

    validation_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()