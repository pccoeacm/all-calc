def calc(should_print=False):

    print("""
    Name: Subtraction 
    Operation : Subtraction of 2 numbers 
    Inputs : a->int/float , b->int/float
    Outputs: c=>a-b ->float
    Author : suyashsonawane  
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))

    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [a - b]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
