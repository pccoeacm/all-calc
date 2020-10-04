def calc(should_print=False):

    print("""
    Name: Area Of A Square
    Operation : Finding Area 
    Inputs : a->int/float , b->int/float
    Outputs: c=>a*a
    Author : varunpusarla  
    \n
    """)

    a = float(input("Enter a >>"))
    

    result = {}
    result['inputs'] = [a]
    result['outputs'] = [a*a]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
