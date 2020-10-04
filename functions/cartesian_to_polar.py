# example for Cartesian to polar coordinates
import numpy as np
import math 
def calc(should_print=False):

    print("""
    Name: Cartesian to polar coordinates
    Operation : Conversion of cartesian coordinates to polar coordinates
    Inputs : x->int/float , y->int/float
    Outputs: r->int/float and Angle->int/float
    Author : Tejasborde2607  
    \n
    """)

    x = float(input("Enter x-coordinate >>"))
    y = float(input("Enter y-coordinate >>"))

    result = {}
    result['inputs'] = [x, y]

    r = np.sqrt(x**2 + y**2)
    p = np.arctan2(y, x)
    deg=math.degrees(p)
    
    result['outputs'] = [r,deg]

    if should_print:
        print(f"Solution : r= {result['outputs'][0]}\n\t   Angle= {result['outputs'][1]}")
    else:
        return result