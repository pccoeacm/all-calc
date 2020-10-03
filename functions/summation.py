def calc(should_print=False):

    print("""
    Name: Summation
    Operation : Summation of square of first n natural numbers 
    Inputs : n->int
    Outputs: o->(n * (n + 1) * (2 * n + 1)) / 6 ->int
    Author : Nityam khandelwal
    \n
    """)

    n = int(input("Enter n >>"))
    result = {}
    result['inputs'] = [n]
    result['outputs'] = [(n * (n + 1) * (2 * n + 1)) / 6]

    if should_print:
        print(f"Solution : {result['outputs'][0]}")
    else:
        return result