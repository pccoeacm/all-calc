

def calc(should_print=False):

    print("""
    Name: Factors
    Operation : Find Factors of number
    Inputs : a->int 
    Outputs: c=>factors(a) ->int
    Author : jessicafernandes
    \n
    """)

    a = int(input("Enter a >>"))
    

    factor=print_factors(a)


    result = {}
    result['inputs'] = [a]
    result['outputs'] = [factor]

    if should_print:
        print(f"Solution {result['outputs']}")
    else:
        return result

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

