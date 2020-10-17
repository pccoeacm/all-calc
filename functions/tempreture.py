def calc(should_print=False):

    print("""
    Name: Temperture Conversion
    Operation : Conversion from celsius to fahrenheit and vice versa 
    Inputs : i->int , x->int/float
    Outputs: z->float
    Author : shreyasd302  
    \n
    """)

    i=int(input("press 1 for celsius to fahrenheit else press 2: "))
    if(i==1):	
	    x = float(input("Enter temperature in celsius: "))
	    y = (x * 9/5) + 32
	    


    else:
	    x = float(input("Enter temperature in fahrenheit: "))
	    y = (x - 32) * 5/9
	    



    result = {}
    result['inputs'] = [i, x]
    result['outputs'] = [y]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
