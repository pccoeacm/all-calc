import math
def calc(should_print=False):
    
    print("""
    Name: trignometric sine value
    Operation : finding the trignometric value of the given input
    Inputs : a->int/float
    Outputs: c=>sin(a) ->float
    Author : UnnatiBhalekar
    \n
    """)

    a = float(input("Enter a >>"))
    c = round(math.sin(a))
    result = {}
    result['inputs'] = [a]
    result['outputs'] = [c]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
print(calc())
