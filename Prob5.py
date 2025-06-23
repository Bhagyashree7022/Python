"""PMI CAlculator
Enter Height and Weight  and calcculate PMI on following cvategory
if PMI <18.5 Print Underweight
if PMI btw 18.5 24.9 print Normal Weight
If PMI brtw 25 to 29.9 print ovwer weight
PMI >30 print OBS
calciulate personal PMI
weight/height^2 """

w=int(input("Enter Weight"))
h=float(input("Enter Height"))
b=w/h**2
if(b<18.5):
    print("Under weight")
elif(b>=18.5 and b<=24.9):
    print("Normal weight")
elif(b>=24.9 and b<=30):
    print("Over weight")
else:
    print("OBS")
