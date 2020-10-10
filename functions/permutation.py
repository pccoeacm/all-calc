import math
def calc(should_print=False):

    print("""
    Name: Permutation
    Operation : Permutation of k over n
    Inputs : n and k -> int
    Outputs: c = perm(n,k)-> int
    Author : Atharva Maid  
    \n
    """)

    n = int(input("Enter n >>"))
    k = int(input("Enter k >>"))
    c = int(math.factorial(n)/(math.factorial(n-k)))
    result = {}
    result['inputs'] = [n, k]
    result['outputs'] = [c]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result