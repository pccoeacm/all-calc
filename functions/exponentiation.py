
def calc(should_print=False):

    print("""
    Name: Exponentiation
    Operation : Take base to the power of exponent 
    Inputs : a->int/float , b->int/float
    Outputs: c=>a^b ->float
    Author : Anirudh Prabhakaran  
    \n
    """)

    a = float(input("Enter a (base) >>"))
    b = float(input("Enter b (exponent) >>"))

    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [a ** b]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result