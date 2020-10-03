def calc(should_print=False):

    # desc
    print("""
    Name: Factorial
    Operation : Calculates factorial of a number 
    Inputs : a->int/float 
    Outputs: c=>a! ->float
    Author : suyashsonawane  
    \n
    """)

    a = float(input("Enter a >>"))

    factorial = 1
    if int(a) >= 1:
        for i in range(1, int(a) + 1):
            factorial = factorial * i

    result = {}
    result['inputs'] = [a]
    result['outputs'] = [factorial]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result


