
def calc(should_print=False):

    print("""
    Name: Harmonic mean
    Operation : Calculate harmonic mean of n observations
    Inputs : n->int, a->int/float
    Output: hmean->float
    Author : dhanashreemunot
    \n
    """)
    
    num_list = []
    sm = 0
    n = int(input("Enter number of observations >>"))
    for i in range(0,n):
        a = float(input(f"Enter number {i + 1} >>"))
        num_list.append(a)
    for i in range(n):
        sm = sm + 1/num_list[i]
    
    hmean = n/sm
    result = {}
    result['inputs'] = [n,a]
    result['outputs'] = [hmean]


    if should_print:
        print('The Harmonic Mean is :'+'{0:.6f}'.format(result['outputs'][0]))
    else:
        return result