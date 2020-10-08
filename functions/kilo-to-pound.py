def calc(should_print=False):

    print("""
    Name: kilo-to-pound converter
    Operation : Kilo to pound converter 
    Inputs : kg->int/float
    Outputs: lbs=>float
    Author : rakshit_jha  
    \n
    """)

    kg = float(input("Enter a >>"))
    lbs = 2.2064 * kg

    result = {}
    result['inputs'] = [kg]
    result['outputs'] = [lbs]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result