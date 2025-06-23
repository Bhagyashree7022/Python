""" create a program take percentage of student if marks
    marks between 80 to 89 Grade B
    marks between 70 to 79 Grade C
    marks between 60 to 69 Grade D
    Below 60 Fail"""

m= int(input("Enter Marks of student :="))
if(m>=90):
    print("Grade A")
elif(m<=89 and m>=80):
    print("Grade B")
elif(m<=79 and m>=70):
    print("Grade C")
elif(m<=69 and m>=60):
    print("Grade D")
else:
    print("Fail")
