def calc(should_print=False):

    print("""
    Name: Modulo
    Operation : Modulo of 2 numbers 
    Inputs : a->int , b->int
    Outputs: c=>a%b ->int
    Author : MEHUL25 
    \n
    """)

    a = int(input("Enter a >>"))
    b = int(input("Enter b >>"))

    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [a % b]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result