import random


class Agent:

    def __init__(self):
        self.knowledge: dict = {0: {'clean': 'right', 'unclean': 'clear'}, 1: {'clean': 'left', 'unclean': 'clear'}}
        self.position: int = random.randint(0, 1)
        self.environment: list = []
        self.score = 0

    def action(self) -> list:
        action: str = self.actuator()

        if action == 'clear':
            self.clear()
        if action == 'right':
            self.move_right()
        if action == 'left':
            self.move_left()

        return self.environment

    def sensor(self, environment: list):
        self.environment = environment

    def actuator(self) -> str:
        return self.knowledge.__getitem__(self.position).__getitem__(self.environment[self.position])

    def clear(self):
        self.environment[self.position] = 'clean'
        self.score += 1

    def move_right(self):
        self.position += 1

    def move_left(self):
        self.position -= 1