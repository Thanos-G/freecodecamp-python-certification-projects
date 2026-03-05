** start of main.py **

import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, quantity in balls.items():
            self.contents.extend([color] * quantity)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            indices = random.sample(range(len(self.contents)), num_balls)
            drawn_balls = [self.contents[i] for i in sorted(indices, reverse=True)]
            for i in sorted(indices, reverse=True):
                del self.contents[i]
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        success = True
        for color, quantity in expected_balls.items():
            if drawn_balls.count(color) < quantity:
                success = False
                break
        if success:
            num_successful += 1
    return num_successful / num_experiments


** end of main.py **

