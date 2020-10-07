# example for internal-angle-calc.py
    
def calc(should_print=False):

    print("""
    Name: Internal Angle Calculator
    Operation : calculate internal angles of n-sided polygon 
    Inputs : n->int/float 
    Outputs: angle=>a+b ->float
    Author : rakshit_jha  
    \n
    """)

    n = float(input("Enter number of sides of polygon >>"))
    if n <= 2: 
        print('Number of sides shall be greater than 2!')
        exit('Invalid Input Detected. Function abort.')
    else:
        angle = 360 / n

    result = {}
    result['inputs'] = [n]
    result['outputs'] = [angle]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result