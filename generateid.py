# Generate an ID
import random


class UserID:
    def __init__(self):
        pass

    def generate_id(self):
        user_id = ''
        for _ in range(8):
            digit = random.randint(0, 9)
            user_id += str(digit)
        return user_id
