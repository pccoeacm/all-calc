from math import *

def calc(should_print=False):
    #steps
    n=10000
    # desc
    print("""
    Name: Integration
    Operation : Calculates Numerical/Definate Integration of any Equation f(x)
    Inputs : a->Lower Limit of Integral (float)
             b->Higher Limit of Integral (float)
             eqn-> Equation in f(x) (string)
    Outputs: result=>Integration Value ->float
    Author : aniketdhole07  
    \n
    """)
    
    #take inputs
    a=float(input("Enter a >>"))
    b=float(input("Enter b >>"))
    eqn=input("Enter eqn >>")
    
    #calculate the stepping difference
    h = (b - a)/float(n)
    result = 0
    #Sum up all the areas under curve using Trapezoidal Integration Algorithm
    for i in range(n):
        x=a + i*h + 0.5*h
        #evaluate equation wrt x
        result += eval(eqn)
    
    #Store the total result with all steps in output
    output= h*result
    
    if should_print:
        print ('result=> : %g' %(output))
    else:
        return output
     