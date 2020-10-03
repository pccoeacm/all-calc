# example for add.py

import math


def calc(should_print=False):

    print("""
    Name: Sigmoid
    Operation : Does the sigmoid ops of given number 
    Inputs : a->int/float
    Outputs: c=>sigmoid(a) ->float
    Author : suyashsonawane  
    \n
    """)

    a = float(input("Enter a >>"))

    c = 1 / (1 + math.exp(-a))

    result = {}
    result['inputs'] = [a]
    result['outputs'] = [c]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result