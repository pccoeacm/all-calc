def calc(should_print=False):

    print("""
    Name: MapValueToRange

    Operation : Maps a value of given range to the value of another range 

    Inputs : original_value         -> int/float, 
             original_min(included) -> int/float,  
             original_max(included) -> int/float, 
             new_min(included)      -> int/float, 
             new_max(included)      -> int/float

    Outputs: new_value -> int/float

    Author : pratik-dhende  
    \n
    """)

    original_value = float(input("Enter original_value >> "))
    original_min = float(input("Enter original_min(included) >> "))
    original_max = float(input("Enter original_max(included) >> "))
    new_min = float(input("Enter new_min(included) >> "))
    new_max = float(input("Enter new_max(included) >> "))

    result = {}
    result['inputs'] = [original_value, original_min, original_max, new_min, new_max]
    result['outputs'] = [(((new_max - new_min) / (original_max - original_min)) * (original_value - original_min)) + new_min]

    if should_print:
        print(f"\nSolution {result['outputs'][0]}")
    else:
        return result