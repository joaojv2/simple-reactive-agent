from Agent import Agent
from Environment import Environment


class Simulator:

    def __init__(self):
        self.environment: Environment = Environment()
        self.agent: Agent = Agent()

    def simulation(self):
        final_score: int = 0
        for _ in range(3):
            self.environment = Environment()
            self.agent = Agent()
            environment: list = self.environment.generate_clean_environment()
            for _ in range(1000):
                environment = self.environment.modify_environment(environment)
                self.agent.sensor(environment)
                environment = self.agent.action()

            print("Score per test -> ", self.agent.score)
            final_score += self.agent.score

        print("Final score -> ", final_score / 3)
