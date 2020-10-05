# example for quit.py
    
def calc(should_print=False):


    import sys
    sys.exit('Exit successful')

    result = {}
    result['inputs'] = []
    result['outputs'] = []

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result

