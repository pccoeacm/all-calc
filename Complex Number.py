def calc(should_print=False):

    print("""
    Name: Complex number Addition
    Operation : Addition of 2 complex numbers 
    Inputs : a->int , b->int
    Outputs: c=>ab ->/int
    Author : RushikeshMarkad16  
    \n
    """)
    
     
    a = complex(int(input("Enter the real number : ")), int(input("Enter the Imaginary number : "))) 
    b = complex(int(input("Enter the real number : ")), int(input("Enter the Imaginary number : "))) 
    print( "Addtion is : ", a+b) 
        
    
    if should_print:
        print("Solution {result['outputs'][0]}")
    else:
        return 0
calc()