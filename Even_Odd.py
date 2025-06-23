"""
#Check no is Even or Odd
n=int(input("Enter number := "))
if n%2==0:
   print(" Number is Even")
else:
    print("Number is Odd")


#Check no is Negative or Positive

n=int(input("Enter number := "))
if n>0:
   print(" Number is Positive")
else:
    print("Number is Negative")


#max of two numbers
n1=int(input("Enter two numbers number := "))
n2=int(input())
if(n1>n2):
    print(f"{n1} is greater than {n2}")
else:
    print(f"{n1} is less than {n2}")

"""
#max of Three numbers
"""
n1=int(input("Enter three numbers number := "))
n2=int(input())
n3=int(input())
if(n1>n2):
      if n1>n3:
       print(f"{n1} is greater than {n2} and {n3}")
      else:
         print(f"{n3} is less than {n2} and {n1}")
else:
    if n2>n3:
        print(f"{n2} is greater than {n1} and {n3}")
    else:
        print(f"{n3} is greater than {n2} and {n1}")
"""

n=int(input("Enter number :="))
if n>0 :
    print(f"{n} Piositive ")
elif(n==0):
    print(f"{n} is 0")
else :
    print(f"{n} is Negative")
"""
n=int(input("Enter number :="))
if(n==1):
          print("Monday")
elif(n==2):
          print("Tuesday")
elif(n==3):
          print("Wednesday")
elif(n==4):
          print("Thursday")
elif(n==5):
          print("Friday")
elif(n==6):
          print("Saturday")
else :
       print("Sunday")   
