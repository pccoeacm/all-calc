def calc(should_print=False):

    print("""
    Name: Area Of Triangle
    Operation : Finding Area 
    Inputs : a->int/float , b->int/float
    Outputs: c=>0.5*a*b ->float
    Author : varunpusarla  
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))

    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [0.5 * a * b]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
