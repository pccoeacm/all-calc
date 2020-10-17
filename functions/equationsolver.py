from math import *
def calc(should_print=False):

		print("""
		Name: Equation Solver
		Operation : Solves Equation in String with variables as x,y,z
		Inputs : eqn-> Enter Any Equatution with variables x,y,z  (string)
			     x->Enter value of x (int)
			     y->Enter Value of y (int)
			     z->Enter value of z (int)
		Outputs: Output of Eveluated Equation
		Author : aniketdhole07  
		\n
		""")


		eqn=input("Enter eqn >>")
		x=int(input("Enter x >>"))
		y=int(input("Enter y >>"))
		z=int(input("Enter z >>"))
		output=eval(eqn)

		if should_print:
				print("Answer: "+str(output))	
		else:
				return output
		 
calc(True)	
