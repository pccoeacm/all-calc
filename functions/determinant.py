import numpy as np 


def calc(should_print=False):

    print("""
    Name: Addition
    Operation : Addition of 2 numbers 
    Inputs : a->float n->float
    Outputs: c=>det(a) ->float
    Author : integral-rip  
    \n
    """)

    n = int(input("Enter order of matrix : "))  
    a = np.array(input("Enter matrix elements separated by space : ").split(' '))
    b = a.reshape(n,n)
    d = np.linalg.det(b)

    result = {}
    result['inputs'] = [a]
    result['outputs'] = [d]

    if True:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result

