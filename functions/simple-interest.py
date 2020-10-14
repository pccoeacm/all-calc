
def calc(should_print=False):

    print("""
    Name: Simple Interest
    Operation : calulate simple interest -> Enter principle, rate, and time.
    Inputs : a->int/float , b->int/float, c->int/float
    Outputs: d->float/int
    Author : TanmaySonawane  
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))
    c = float(input("Enter c >>"))

    d = (a * b * c) / 100

    result = {}
    result['inputs'] = [a, b, c]
    result['outputs'] = [d]


    if should_print:
        print('The Simple interest is  {0}'.format(d))
    else:
        return result