"""
String
->is collection of characaters
->boundary is "" ''
->is immutable data type

->methods:=
"""
s="a"
str="Bhagya"
print(len(s))
print(len(str))

#alphabet cases
print(str.lower())
print(str.upper())
str="BhAgyA"
print(str.swapcase())
str="bhagya"
print(str.capitalize())

"""
index and find are same ->only index return error if char not present
                        ->but find return -1
"""
#indexing
print(str.index("a"))#it return index of specified character in string from left
print(str.rindex("a"))
#print(str.rindex("c"))#return substring not found
print(str.find("g"))#also return index
print(str.rfind("a"))
print(str.rfind("c"))#return -1  if not present char

print(str.replace("b","s"))#replace b by s
list=["a","e","i","o","u"]
print("*".join(list))#used to join strings
str='p'
print(str.join(list))
str="i am student"
print(str.split())#by default takes " " as split parameter 
str="bhagyashree"
print(str.split("a"))
str=" bhagya "
print(str.strip())
print(str.lstrip())#remove space from left
print(str.rstrip())#remove space from right

"""
Boolean methods
"""
str= input("Enter char :=")
if(str.isalpha()):#return  true or false
    print("its charater")#return  true or false
elif(str.isdigit()):
    print("its numebe5r")
elif str.isalnum():
    print("its alphanumeric")
elif str.isalnum():
    print("its alphanumeric")

else:
        print("its symbol")

str= input("Enter char :=")       
if str.islower():
    print("its lowercase")
else:
        print("its uppercase")
  

"""
LIST =>
->Collection of heterogenous and homogenous elements
->its mutable datatype
->its boundary []
->henece we add elements and remove elements 
"""

