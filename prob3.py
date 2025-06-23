"""calculate electricity based on units 
  for first 100 unit rs. 3.05/unit
  next 100 units 4.5/units
  next 100 units 5.5/units
  above 500 unit 7.5/units"""

units = int (input("Enter Units := "))
if units<=100:
            bill=units*3.5;
elif units<=200:
            bill=(units-100)*4.5 +100*3.5
elif(units<=300):
            bill=(units-200)*5.5 +100*4.5+100*3.5
elif units<=400:
            bill=(units-300)*6.5 + 100*5.5 +100*4.5+100*3.5
else:
    bill=(units-500)*7.5 + 100*6.5 +100*5.5 +100*4.5+100*3.5

         
print(bill)
