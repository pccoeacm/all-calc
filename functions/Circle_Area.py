def calc(should_print=False):

    print("""
    Name: Area Of Circle
    Operation : Finding Area 
    Inputs : a->int/float 
    Outputs: c=>3.14*a*a ->float
    Author : varunpusarla  
    \n
    """)

    a = float(input("Enter a >>"))
 

    result = {}
    result['inputs'] = [a]
    result['outputs'] = [3.14 * a * a]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
