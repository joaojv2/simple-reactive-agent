import random


class Environment:

    @staticmethod
    def generate_clean_environment() -> list:
        return ['clean' for _ in range(2)]

    def modify_environment(self, environment: list) -> list:
        if random.randint(0, 1) == 1:
            positions: list = self.get_clean_positions(environment)
            if positions.__len__() == 1:
                environment[positions.__getitem__(0)] = 'unclean'
            elif positions.__len__() == 2:
                if random.randint(0, 1) == 0:
                    environment = ['unclean' for _ in range(environment.__len__())]
                else:
                    environment[positions.__getitem__(random.randint(0, 1))] = 'unclean'
        return environment

    @staticmethod
    def get_clean_positions(environment: list) -> list:
        return [x for x in range(environment.__len__()) if environment[x] == 'clean']
