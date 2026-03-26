from string_validation_interfaces.srv import Str

import rclpy
from rclpy.node import Node

class StringValidationService(Node):
    def __init__(self):
        super().__init__('string_validation_service')
        self.srv = self.create_service(Str, 'string_validation', self.validate_string)

    def validate_string(self, req, res):
        res.is_valid = self.validate_capitalization(req.str)
        return res

    def validate_capitalization(self, text):
        if not text:
            return True
        
        words = text.split()
        
        for i, word in enumerate(words):
            if not word:
                continue
                
            clean_word = ''.join(c for c in word if c.isalpha())
            
            if not clean_word:
                continue
            
            if i == 0:
                if not (clean_word.isupper() or (clean_word[0].isupper() and clean_word[1:].islower())):
                    return False
            else:
                if not (clean_word.isupper() or clean_word.islower() or (clean_word[0].isupper() and clean_word[1:].islower())):
                    return False
        
        return True  
    
def main():
    rclpy.init()

    str_service = StringValidationService()

    rclpy.spin(str_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()