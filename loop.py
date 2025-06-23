"""
Loop
loop=> task perform repeatedly for particular times
diff if & while => while executes util condition true if execute when condition true
while=>entry contro
do while => exit control
"""
"""
i=1
while i<=10:
    print(i)
    i=i+1
    print("End of while")
else:
    print(0)

n=int(input("Enter number := "))
i=1
while i<=10:
    print(f"{n} X {i} =",n*i)
    i=i+1

# 1 to 10 Even number
print("1 to 100 Even numbers :=")
i=1
while i<=10:
    if i%2==0:
         print(i)
    i=i+1

# 1 to 10 odd number
print("1 to 100 Odd numbers :=")
i=1
while i<=10:
    if i%2!=0:
         print(i)
    i=i+1

#factorial number
n=int(input("Enter number := "))
i=n
fact=1
while i>=1:
    fact=fact*i
    i=i-1
print(fact)

#calculate prime number
n=int(input("Enter number := "))
i=2
flag=True
while(i<n/2):
    if n%i==0:
        flag=False
        break
    i=i+1
if flag:
    print(f"{n}   prime")
else:
    print(f"{n} is not  prime")

#using range factorial
n=int (input("Enter number "))
fact=1
i=1
for i in range (1,n+1):
    fact=fact*i
print(fact)
"""
count=1
for i in range (1,4):
    for j in range (1,4):
        print(count,end=' ')
        count=count +1
    print()
    


