# example for mean.py
    
def calc(should_print=False):

    print("""
    Name: Mean
    Operation : Mean of n numbers 
    Inputs : a->int/float , b->int/float
    Outputs: mean=> sum / n ->float
    Author : rakshit_jha
    \n
    """)
    nums = list()
    sum = 0
    n = float(input("Enter count of numbers to calculate mean >>"))
    for x in range(int(n)):
        a = float(input(f"Enter number {x + 1} >>"))
        nums.append(a)
    for num in nums:
        sum = int(num) + sum
        mean = sum / n
    result = {}
    result['inputs'] = [n, a]
    result['outputs'] = [mean]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result