def calc(should_print=False):

    print("""
    Name: Perimeter Of Triangle
    Operation : Finding Perimeter 
    Inputs : a->int/float b->int/float 
    Outputs: d=>a+b+c ->float
    Author : varunpusarla  
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))
    c = float(input("Enter c >>"))
 

    result = {}
    result['inputs'] = [a,b,c]
    result['outputs'] = [a + b + c]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
