"""Simulate tyraffuiicv signal where user inputs the color and program gives instruction
if red Print "Stop"
if yellow "Gert Ready"
if Green "Go"
any other inpour "Invalid Color"
"""

clr=input("Enter color := ")
if(clr=="Red" and clr=="red" ):
    print("Stop")
elif(clr=="Yellow" and clr=="yellow"):
    print("Get Ready")
elif(clr=="Green" and clr=="green"):
    print("GO")
else :
    print("Invalid color")
