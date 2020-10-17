def calc(should_print=False):

    print("""
    Name: Distance convertor
    Operation : Converts feet into inches, yards and miles 
    Inputs : ft->float
    Outputs: inches, yards, miles ->float
    Author : shreyasd302
    \n
    """)

    
   

    ft = int(input("Input distance in feet: "))
    inches = ft * 12
    yards = ft / 3.0
    miles = ft / 5280.0

    x=("The distance in inches is %i inches." % inches)
    y=("The distance in yards is %.2f yards." % yards)
    z=("The distance in miles is %.2f miles." % miles)
    p= (x,y,z)

    result = {}
    result['inputs'] = [ft]
    result['outputs'] = [p]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
