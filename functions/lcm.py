def calc(should_print=False):

    print("""
    Name: LCM(Least common multiple)
    Operation : LCM of 2 numbers
    Inputs : a->int , b->int
    Outputs: c=>lcm(a,b) ->int
    Author : suyashsonawane
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))
    if(a > b ):   # Use If condition to find the greatest number among these two.
        max= a
    else:
        max= b
    while(True):
        if(max % a == 0 and max % b == 0):
            print(max)
            break;
        max= max+ 1


    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [max]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
