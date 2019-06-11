import re


class Calculator:

    @staticmethod
    def add(inputs: str):
        delimiters = r'[,\n]'
        if len(inputs) == 0:
            return 0
        if not re.match(r'[.\d]', inputs.split('\n')[0]):
            delimiters = inputs.split('\n')[0]
            inputs = "\n".join(inputs.split('\n')[1:])
        inputs_list = list(re.split(delimiters, inputs))
        inputs_float_list = list(map(float, inputs_list))
        if any([i < 0 for i in inputs_float_list]):
            raise Exception("negatives not allowed ")
        # print(f"""Call with :
        # \t- delimiters={delimiters}
        # \t- inputs={inputs}
        # \t- inputs_list={inputs_list}
        # \t- inputs_float={inputs_float_list}""")
        return sum(inputs_float_list)

