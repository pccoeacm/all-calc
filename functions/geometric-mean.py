import math

def calc(should_print=False):

    print("""
    Name: Geometric mean
    Operation : Calculate geometric mean of n observations
    Inputs : n->int, a->int/float
    Output: gmean->float
    Author : dhanashreemunot
    \n
    """)
    
    num_list = []
    prod = 1
    n = int(input("Enter number of observations >>"))
    for i in range(0,n):
        a = float(input(f"Enter number {i+1}>>"))
        num_list.append(a)
    for i in range(n):
        prod = prod * num_list[i]
    
    gmean = (math.pow(prod, (1 / n)))
    result = {}
    result['inputs'] = [n,a]
    result['outputs'] = [gmean]


    if should_print:
        print('The Geometric Mean is :'+'{0:.6f}'.format(result['outputs'][0]))
    else:
        return result