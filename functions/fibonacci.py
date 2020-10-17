def calc(should_print=False):

    print("""
    Name: Fibonacci 
    Operation : Fibonacci of n numbers 
    Inputs : a->int
    Outputs: b->int
    Author : sanketchaudhari10
    \n
    """)


    # input
    a = int(input("Fibonacci for number of terms:  "))
    result = {}
    result['inputs'] = [a]

    #code
    if (a <= 0):
        sum = 0

    else:

        if a<=2:
            sum = 1

        else:
            sum=0
            b =1
            c=1
            for i in range(2, a ):
                sum =  b + c
                b= c
                c = sum

    result['outputs'] = [sum]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result

