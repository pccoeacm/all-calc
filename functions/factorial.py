def calc(should_print=False):

    print("""
    Name: Factorial
    Operation: Factorial of given integer
    Inputs: n->int
    Output: fac->int
    Author: ShamikG17
    \n
    """)

    n = int(input("Enter n >> "))
    fac = 1

    while(n > 1):
        fac = fac*n
        n -= 1

    result = {}
    result['inputs'] = [n]
    result['outputs'] = [fac]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
    
    