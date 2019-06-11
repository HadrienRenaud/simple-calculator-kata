import re


class Calculator:

    @staticmethod
    def add(inputs: str):
        if len(inputs) == 0:
            return 0
        if re.match(r'^//.+$', inputs.split('\n')[0]):
            delimiters = inputs.split('\n')[0][2:]
            print("Custom delimiters :", delimiters)
            inputs = "\n".join(inputs.split('\n')[1:])
            inputs_list = list(inputs.split(delimiters))
        else:
            inputs_list = list(re.split(r'[,\n]', inputs))
        inputs_float_list = list(map(float, inputs_list))
        if any([i < 0 for i in inputs_float_list]):
            raise Exception("negatives not allowed ")
        inputs_filtered = list(filter(lambda x: x < 1001, inputs_float_list))
        # print(f"""Call with :
        # \t- delimiters={delimiters}
        # \t- inputs={inputs}
        # \t- inputs_list={inputs_list}
        # \t- inputs_float={inputs_float_list}""")
        return sum(inputs_filtered)

