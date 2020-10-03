def bina(n):
    l1=[]
    num=n
    rem=0
    while(num>0):
        rem=num%2
        num=num//2
        l1.append(str(rem))
    l1.reverse()
    str1="".join(l1)
    return str1

def octa(n):
    l1=[]
    num=n
    rem=0
    while(num!=0):
        rem=num%8
        num=num//8
        l1.append(str(rem))
    l1.reverse()
    str1="".join(l1)
    return str1

def hexa(n):
    l1=[]
    num=n
    rem=0
    dict={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while(num!=0):
        rem=num%16
        num=num//16
        if rem in range(0,10):
           l1.append(str(rem))
        else:
            l1.append(dict[rem])
    l1.reverse()
    str1="".join(l1)
    return str1

def calc(should_print=False):
    print("1.Decimal to binary\n2.Decimal to Hexadecimal\n3.Decimal to Octal")
    choice = int(input("Enter your choice: "))
    n=int(input("Enter a decimal number: "))
    if choice==1:
        if should_print:
            print("Binary conversion is: ",bina(n))
        else:
            return bina(n)
    elif choice==2:
        if should_print:
            print("Hexadecimal conversion is: ",hexa(n))
        else:
            return hexa(n)
    elif choice==3:
        if should_print:
            print("Octal conversion is: ", octa(n))
        else:
            return octa(n)
    else:
        if should_print:
            print("Please enter valid choice")
        else:
            return None