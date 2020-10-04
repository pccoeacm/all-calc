def calc(should_print=False):

    print("""
    Name: Perimeter Of Rectangle
    Operation : Finding Perimeter 
    Inputs : a->int/float b->int/float 
    Outputs: c=>2(a+b) ->float
    Author : varunpusarla  
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))
 

    result = {}
    result['inputs'] = [a]
    result['outputs'] = [2*(a+b)]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
