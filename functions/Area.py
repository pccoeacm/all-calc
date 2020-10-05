

def calc(should_print=False):

    print("1. Square Area")
    print("2. Square Perimeter")
    print("3. Circle Area")
    print("3. Circle Perimeter")
    print("5. Triangle Area")
    print("6. Triangle Perimeter")
    print("7. Rectangle Area")
    print("8. Rectangle PErimeter")
    print("9. Exit ")



    loop=True


  
       
  
    while loop:


            
        choice = float(input("Enter your choice [1-6]: "))
     
        if choice==1: 

            print("""
            Name: Sqaure Area
            Operation : Finding Area 
            Inputs : a->int/float 
            Outputs: c=>a*a ->float
            Author : varunpusarla  
            \n
            """)
            
            a = float(input("Enter a >>"))
            result = {}
            result['inputs'] = [a]
            result['outputs'] = [a*a]
            loop=False
        
        elif choice==2:

            print("""
            Name: Sqaure Perimeter
            Operation : Finding Perimeter
            Inputs : a->int/float  
            Outputs: c=>4*a ->float
            Author : varunpusarla  
            \n
            """)
            a = float(input("Enter a >>"))
       
            result = {}
            result['inputs'] = [a,b]
            result['outputs'] = [4*a]
            loop=False

        elif choice==3:
            
            print("""
            Name: Circle Area
            Operation : Finding Area
            Inputs : a->int/float 
            Outputs: c=>3.14*a*a ->float
            Author : varunpusarla  
            \n
            """)
            a = float(input("Enter a >>"))
            result = {}
            result['inputs'] = [a]
            result['outputs'] = [3.14*a*a]
            loop=False

        elif choice==4:
            
            print("""
            Name: Circle Perimeter
            Operation : Finding Perimeter
            Inputs : a->int/float 
            Outputs: c=>2*3.14*a ->float
            Author : varunpusarla  
            \n
            """)
            a = float(input("Enter a >>"))
            result = {}
            result['inputs'] = [a]
            result['outputs'] = [2*3.14*a]
            loop=False

        elif choice==5:
            
            print("""
            Name: Triangle Area
            Operation : Finding Area
            Inputs : a->int/float b->float/int
            Outputs: c=>0.5*a*b ->float
            Author : varunpusarla  
            \n
            """)
            a = float(input("Enter a >>"))
            b = float(input("Enter b >>"))
            result = {}
            result['inputs'] = [a,b]
            result['outputs'] = [0.5*a*b]
            loop=False

        elif choice==6:

            print("""
            Name: Triangle Perimeter
            Operation : Finding Perimeter
            Inputs : a->int/float b->float/int c->float/int
            Outputs: c=>a+b+c ->float
            Author : varunpusarla  
            \n
            """)
            a = float(input("Enter a >>"))
            b = float(input("Enter b >>"))
            c = float(input("Enter c >>"))
            result = {}
            result['inputs'] = [a,b,c]
            result['outputs'] = [a+b+c]
            loop=False

        elif choice==7:
            print("""
            Name: Rectangle Area
            Operation : Finding Area
            Inputs : a->int/float b->float/int 
            Outputs: c=>a*b ->float
            Author : varunpusarla  
            \n
            """)
            a = float(input("Enter a >>"))
            b = float(input("Enter b >>"))
        
            result = {}
            result['inputs'] = [a,b,c]
            result['outputs'] = [a*b]
            loop=False

        elif choice==8:
            print("""
            Name: Rectangle Perimeter
            Operation : Finding Perimeter
            Inputs : a->int/float b->float/int 
            Outputs: c=>2*(l+b) ->float
            Author : varunpusarla  
            \n
            """)
            a = float(input("Enter a >>"))
            b = float(input("Enter b >>"))
            result = {}
            result['inputs'] = [a]
            result['outputs'] = [2*(l+b)]
            loop=False

        elif choice==9:
            loop=False


        else:
        # Any integer inputs other than values 1-5 we print an error message
            float(input("Wrong option selection. Enter any key to try again.."))

    if should_print:
        print(f"Solution {result['outputs'][0]}")


        
    else:
        return result

 
          
