
class Calculator:

    @staticmethod
    def add(inputs: str):
        if len(inputs) == 0:
            return 0
        inputs_list = inputs.split(',')
        return sum(map(float, inputs_list))
