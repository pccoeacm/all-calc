import cmath


def calc(should_print=False):

    print("""
    Name: Quadratic Solver
    Operation : Solves a quadratic equation of format ax^2 + bx + c =0
    Inputs : a->int/float , b->int/float , c->int/float
    Outputs: x1,x2 ->complex / real
    Author : suyashsonawane  
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))
    c = float(input("Enter c >>"))

    d = (b**2) - (4 * a * c)

    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    result = {}
    result['inputs'] = [a, b, c]
    result['outputs'] = [sol1, sol2]

    if should_print:
        print('The solution are {0} and {1}'.format(sol1, sol2))
    else:
        return result
