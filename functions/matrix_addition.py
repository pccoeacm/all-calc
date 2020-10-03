import numpy as np

def calc(should_print=False):

    print("""
    Name: Matrix Addition
    Operation : Addition of 2 matrices 
    Inputs : a->int/float , b->int/float
    Outputs: c=>a+b ->np.array
    Author : varunpusarla  
    \n
    """)

# number of elements 
    n = int(input("Enter number of elements : ")) 
  
# Below line read inputs from user using map() function  
    a_temp = list(map(int,input("\nEnter the numbers for a : ").strip().split()))[:n] 
    b_temp = list(map(int,input("\nEnter the numbers for b : ").strip().split()))[:n] 
  
    print("\n Matrix A - ", a_temp) 
    print("\n Matrix B - ", b_temp) 

    a= np.array(a_temp)
    b= np.array(b_temp)


    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = np.add(a,b)

    if should_print:
        print(f"Solution {result['outputs'][0]}")

    else:
        print(result)

     

