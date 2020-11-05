    # example for hypotenuse.py
    
def calc(should_print=False):

    print("""
    Name: Hypotenuse Length
    Operation : Finding length of the hypotenuse 
    Inputs : a->int/float , b->int/float
    Outputs: c=>((a**2) + (b**2))**0.5 ->float
    Author : rajkumawat  
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))

    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [((a**2) + (b**2))**0.5]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result