
from re import split

class Calculator:

    @staticmethod
    def add(inputs: str):
        if len(inputs) == 0:
            return 0
        inputs_list = split(r'[,\n]', inputs)
        return sum(map(float, inputs_list))
