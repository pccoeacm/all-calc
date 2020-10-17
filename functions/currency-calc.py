from forex_python.converter import CurrencyRates
def calc(should_print=False):

    print("""
    Name:Currency Calculator
    Operation : cuurency calculation
    Inputs : a->string,b->string,x->int/float
    Outputs: y=>conversion of currency ->float
    Author : Apoorva-Datir
    \n
    """)


    c = CurrencyRates()
    a=input("enter original currency(e.g. USD): ")
    b=input("enter second currency(e.g. INR): ")
    x= float(input("enter amount: "))
    y=c.convert(a, b, x)
    print("{} {} = {} {}".format(x,a,y,b))



    result = {}
    result['inputs'] = [a, b, x]
    result['outputs'] = [y]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
