"""username=input("Enter your name : ")
print("My name is := "+ username)

age=int(input("Enter your age :="))
print("My name is := ",age)

#here input treated as string hence it concate two numbers so ans is different 
n1=(input("Enter 1st number :="))
n2=(input("Enter 1st number :="))
sum=n1+n2
print("Addition is = ",sum)

n1=int(input("Enter 1st number :="))
n2=int(input("Enter 1st number :="))
sum=n1+n2

print("Addition of ",n1," and ",n2," is  = ",sum)
print("Substraction of ",n1," and ",n2," is  = ",(n1-n2))
print("Multiplication of ",n1," and ",n2," is  = ",(n1*n2))
print("Division of ",n1," and ",n2," is  = ",(n1/n2))
print("Remainder of ",n1," and ",n2," is  = ",(n1%n2))
print("Float Division  of ",n1," and ",n2," is  = ",(n1//n2))
print("Exponential of ",n1," and ",n2," is  = ",(n1**n2))
"""

age=int(input("Enter your age :="))
txt="My age = {age}" 
print(txt)
#O/P=>My age = {age}
#without f it cant give value of age

age=int(input("Enter your age :="))
txt=f"My age = {age}"# without f it cant give value of age 
print(txt)

n1=int((input("Enter 1st number :=")))
n2=int((input("Enter 1st number :=")))
sum=n1+n2
str = f"addition of {n1} and {n2}={sum}"
print(str)
