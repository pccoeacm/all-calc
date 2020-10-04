def calc(should_print=False):

    print("""
    Name: Perimeter Of Square
    Operation : Finding Perimeter 
    Inputs : a->int/float 
    Outputs: c=>4*a ->float
    Author : varunpusarla  
    \n
    """)

    a = float(input("Enter a >>"))
 

    result = {}
    result['inputs'] = [a]
    result['outputs'] = [4*a]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
