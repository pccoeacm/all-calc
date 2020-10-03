def calc(should_print=False):

    print("""
    Name: GCD(Greatest Common Divisor) using Euclid's Algorithm
    Operation : GCD of 2 numbers 
    Inputs : a->int , b->int
    Outputs: c=>gcd(a,b) ->int
    Author : MEHUL25  
    \n
    """)

    a = int(input("Enter a >>"))
    b = int(input("Enter b >>"))

    result = {}
    result['inputs'] = [a, b]

    while(b): 
       a, b = b, a % b 

    result['outputs'] = [a]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result