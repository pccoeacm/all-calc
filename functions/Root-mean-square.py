import math
def calc(should_print=False):

    print("""
    Name: Root mean square function
    Operation : Root mean square of given list of numbers
    Inputs : list -> int
    Outputs: Root mean square of list ->float
    Author : Apoorva-Datir
    \n
    """)

    n = int(input("Enter number of elements : "))
    a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
    square = 0
    mean = 0.0
    root = 0.0
    for i in range(0,n):

        #calculate square
        square += (a[i]**2)

        #calculate mean
        mean = (square / (float)(n))

        #calculate root
        root = math.sqrt(mean)


    print("\nThe Root mean square of numbers is :",root)

    result = {}
    result['inputs'] = [n]
    result['outputs'] = [root]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
