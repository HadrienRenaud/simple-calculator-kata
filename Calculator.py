import re


class Calculator:

    @staticmethod
    def add(inputs: str):
        delimiters=r'[,\n]'
        if len(inputs) == 0:
            return 0
        if not re.match(r'[.\d-]', inputs.split('\n')[0]):
            delimiters = inputs.split('\n')[0]
            inputs = "\n".join(inputs.split('\n')[1:])
        inputs_list = re.split(delimiters, inputs)
        return sum(map(float, inputs_list))

