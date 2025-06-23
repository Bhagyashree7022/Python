"""
WAP to Charge ,mobile deduct balance after the each call until recharge balance run out
take call duration as input
set call cost/unit as 0.75 rs
if bal>0 then user able to make calls otherwise display bal is 0
"""

bal=int(input("Enter recharge balance :=  "))
rate=0.75
while(bal>0.75):
     call=int(input("Enter duration := "))
     total=call*rate
     bal=bal-total
else:
    print("bal is 0")
    
        
    
