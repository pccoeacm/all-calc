def calc(should_print=False):

    print("""
    Name: Average
    Operation : Average of given number
    Inputs :(a,b,c.....n)->int/float ,total no ->int
    Outputs: A=>(a+b+...n)/total_no ->float
    Author : Anand76666  
    \n
    """)
def Average():
    
    Total_list=[]
    total_no = int(input("Enter the total no inputs :"))
    for i in range (0,total_no):
        print("Enter the no",i+1,":")
        b=int(input())
        Total_list.append(b)
    print("Average of given inputs :",sum(Total_list) / len(Total_list))
    return sum(Total_list) / len(Total_list)
    
    if should_print:
        print("Solution {result['outputs'][0]}")
    else:
        return result
        
Average()