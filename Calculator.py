
class Calculator:

    @staticmethod
    def add(inputs: str):
        if len(inputs) == 0:
            return 0
        inputs_list = inputs.split(',')
        if len(inputs_list) == 1:
            return float(inputs_list[0])
        else:
            return float(inputs_list[0]) + float(inputs_list[1])
