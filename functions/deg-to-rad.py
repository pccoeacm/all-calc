def calc(should_print=False):

    print("""
    Name: Degree to Radian Converter
    Operation : Converts an entered value in degrees to radians
    Inputs : degree->int/float
    Outputs: radian ->int/float
    Author : suyashsonawane
    \n
    """)
    pi=22/7

    degree = float(input("Enter a >>"))

    radian = degree*(pi/180)

    result = {}
    result['inputs'] = [degree]
    result['outputs'] = [radian]
    if should_print:
        print("The answer in radians is :{0}".format(radian))
    else:
        return result
