from plotly import graph_objects as go
from math import *

def calc(should_print=False):

		print("""
    Name: 3D Plotter
    Operation : Plots 3D Graph of any 3D Equation z=f(x,y)
    Inputs : size->Size of 3D chart (int)
             eqn-> 3D Equation in f(x,y) (string)
    Outputs: 3D Figure Will be Opened
    Author : aniketdhole07  
    \n
    """)

		size=int(input("Enter size >>"))
		eqn=input("Enter eqn >>")

		z=[]
		#Taverse and Evaluate the Z -Axis based on Equation
		for i in range(size):
			z_tmp=[]
			x=i
			for j in range(size):
				y=j
				z_tmp.append(eval(eqn))
			z.append(z_tmp)

		#x-y 3D Axis Build Points
		x=[]
		y=[]
		for i in range(size):
			x_tmp=[j for j in range(size)]
			x.append(x_tmp)
			y_tmp=[i for j in range(size)]
			y.append(y_tmp)	

		#Plot 3D Figure
		if should_print:
				fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)]) 
				fig.show()
		else:
				return fig
		 

	