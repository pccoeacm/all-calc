import math

def calc(should_print=False):
	print("""
	Name: Trigonometric Operations
	Operation : Provides the results for sin, cos and tan 
	Inputs : a->int/float
	Outputs: sin, cos, tan-> float
	Author : palakg01
	\n
	""")

	x=float(input("Enter value in degrees:"))
	p=math.pi
	sol1=round((math.sin((x*p)/180)),4)
	sol2=round((math.cos((x*p)/180)),4)
	sol3=round((math.tan((x*p)/180)),4)

	result = {}
	result['inputs'] = [x]
	result['outputs'] = [sol1,sol2,sol3]

	if should_print:
	    print(f"sin({x})={result['outputs'][0]}")
	    print(f"cos({x})={result['outputs'][1]}")
	    print(f"tan({x})={result['outputs'][2]}")
	else:
	    return result


