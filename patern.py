"""
* * *
* * *
* * *
"""
i=1
for i in range (1,4):
    for j in range (1,4):
        print("*",end=' ')
    print()
"""
*
* *
* * *
"""
print()
i=1

for i in range (1,4):
    for j in range (i):
        print("*",end=' ')
    print()

"""
* * *
* *
*
"""
print()
i=3
for i in range (1,4):
    for j in range (4-i):
        print("*",end=' ')
    print()

"""
1
2 2
3 3 3
"""

print()
count=1
for i in range(1,4):
    for j in range (1,i+1):
        print(count,end=' ')
    print()
    count=count+1
print()

"""    
1
2 3
4 5 6

"""
count=1
for i in range(1,4):
    for j in range (1,i+1):
        print(count,end=' ')
        count=count+1
    print()
print()

"""
    *
  * * *
* * * * *
i=row,j=space,k=col
"""
i=1
for i in range (1,4):
    for j in range (3-i):
      print(" ",end=' ')
    for k in range (2*i-1):
        print("*",end=' ') 
    print()
print()

"""
str=input("Enter word :=")
c=input("Enter character := ")
if(c in str):
    print("yes present")
else:
    print("not present ")


str=input("Enter word :=")
c=input("Enter character := ")
for i in str:
    if i==ch
    print(f"{c} is present")
    break
    i=i+1
print(f"{c} is not present")

"""
str=input("Enter word :=")
for i in  str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print(i,end=' ')
