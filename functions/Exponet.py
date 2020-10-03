def calc(should_print=False):

    print("""
    Name: Exponent
    Operation : Exponential of 2 numbers 
    Inputs : a->int/float , b->int/float
    Outputs: c=>a**b ->float
    Author : Anand76666  
    \n
    """)
    
    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))
    print("Solution {a**b}>>",a**b)
        
    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [a ** b]
    
    if should_print:
        print("Solution {result['outputs'][0]}")
    else:
        return result
calc()