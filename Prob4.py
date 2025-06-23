""" loan interest based on civil score per annum
if >=750 then Interestb rate is 8%
if between 700 to 759  then Interestb rate is 10%
if between 650 to 699  then Interestb rate is 12%
if below 650 then Interestb rate is 15%"""

p=int(input("Enter Principal units ="))
c=int(input("enter civil Score :="))
n=int(input("Enter year :="))
if(c>=750):
            amt=p*0.08 *n + p
elif(c>=700 and c<=759):
            amt=p*0.1 *n + p
elif(c>=650 and c<=699):
            amt=p*0.12 *n + p
elif(c>650):
            amt=p*0.15 *n + p      
print(amt)
