def calc(should_print=False):

    print("""
    Name: Reciprocal Calculator
    Operation : Reciprocal of 1 number
    Inputs : n->int/float
    Outputs: r=>float
    Author : rakshit_jha  
    \n
    """)

    n = float(input("Enter n >>"))
    r = 1 / n

    result = {}
    result['inputs'] = [n]
    result['outputs'] = [r]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result