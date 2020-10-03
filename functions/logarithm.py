# example for logarithm.py
import math   
def calc(should_print=False):

    print("""
    Name: Logarithm
    Operation : Logarithm of a given number with input base
    Inputs : a->int/float , b->int/float
    Outputs: c=>log(a,b) ->float
    Author : ItsAvi165  
    \n
    """)
    
    a = float(input("Enter Value >>"))
    b = float(input("Enter Base >>"))
    c=math.log(a,b)
    print(c)
    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [c]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
calc()
