def calc(should_print=True):

    print("""
    Name: Addition
    Operation : Addition of 2 numbers 
    Inputs : a->int/float , b->int/float
    Outputs: c= a**b
    Author : Rohan  
    \n
    """)

    a = float(input("Enter Base >> "))
    b = float(input("Enter Exponent (only value/ No fraction)>> "))

    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [a**b]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result

