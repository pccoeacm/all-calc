def bmi():
    a=float(input("Enter height >>"))
    b=float(input("Enter weight >>"))
    ans=b/(a*a)
    print("Your BMI is",ans)
    return ans
bmi()