

def calc(should_print=False):

    print("""
    Name: Profit-Loss
    Operation : To find Profit/Loss 
    Inputs : CP->int/float , SP->int/float
    Outputs: c=>profit/loss ->float
    Author : jessicafernandes
    \n
    """)

    a = float(input("CP >>"))
    b = float(input("SP >>"))

    c=Out(a,b)

    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [c]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result


def Profit(cp, sp) : 
    profit = (sp - cp) 
    return profit 
  
def Loss(cp, sp) : 
    Loss = (cp - sp) 
    return Loss 

def Out(cp,sp) :
    if sp==cp:
        print("No profit nor Loss")

    elif sp > cp : 
        print(Profit(cp,sp), "Profit") 

    else : 
        print(Loss(cp,sp), "Loss") 


