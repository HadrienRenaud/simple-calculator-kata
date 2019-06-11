import re


class Calculator:

    @staticmethod
    def add(inputs: str):
        if len(inputs) == 0:
            return 0
        delimiters = r'[,\n]'
        if re.match(r'^//.+$', inputs.split('\n')[0]):
            delimiters = inputs.split('\n')[0][2:]
            m = re.match(r'^\[(.*)]\[(.*)]$', delimiters)
            if m:
                deli1 = re.escape(m.group(1))
                deli2 = re.escape(m.group(2))
                delimiters = f"{deli1}|{deli2}"
            else:
                delimiters = re.escape(delimiters)
            inputs = "\n".join(inputs.split('\n')[1:])
            # print("Custom delimiters :", delimiters)
        inputs_list = list(re.split(delimiters, inputs))
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

