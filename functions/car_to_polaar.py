import cmath
def calc(should_print=False):

    print("""
    Name: polar_to_cartesian
    Operation : conversion of polar cordinates to rectangular cordinates
    Inputs : a->int/float , b->int/float
    Outputs: c=>rectangular cordinates
    Author : UnnatiBhalekar
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))
    
    cn = complex(a,b)
    # get polar coordinates
    print("Polar Coordinates: ",cmath.polar(cn))

    # polar to rectangular. Format for input is (length, ‹angle in radians›).
    #Returns a complex number
    cn1 = cmath.rect(2, cmath.pi)
    print("Polar to rectangular: ",cn1)
    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [cn1]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
print(calc())
