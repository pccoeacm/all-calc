# example for add.py
    
def calc(should_print=False):

    print("""
    Name: Pythagorean Triplet Checker
    Operation : Pythagorean Triplet Checker
    Inputs : a->int/float , b->int/float, c->int/float
    Outputs: ans->boolean
    Author : rakshit_jha
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))
    c = float(input("Enter c >>"))
    lhs = (a**2) + (b**2)
    rhs = (c**2)

    if lhs == rhs:
        ans = True

    else:
        ans = False

    result = {}
    result['inputs'] = [a, b, c]
    result['outputs'] = [ans]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result