import cmath
from fractions import Fraction
def calc(should_print=False):

    print("""
    Name: float to fraction converter
    Operation : conversion of float to fraction of the given input
    Inputs : a->float
    Outputs: c= fraction of input
    Author : UnnatiBhalekar
    \n
    """)

    a = float(input("Enter a >>"))
    
    value = a
    answer = Fraction(value).limit_denominator()
    print(answer)
    
    result = {}
    result['inputs'] = [a]
    result['outputs'] = [answer]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result

