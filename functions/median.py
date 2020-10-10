import statistics
def calc(should_print=False):

    print("""
    Name: Median
    Operation : Median of a list 
    Inputs : a->float
    Outputs: b=>median of list a ->float
    Author : suyashsonawane  
    \n
    """)

    
   

    a = list(map(float, input("Enter a multiple value: ").split()))

    b= statistics.median(a)

    result = {}
    result['inputs'] = [a]
    result['outputs'] = [b]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
