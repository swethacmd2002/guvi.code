cash=int(input("Enter your full amount: "))
notes=[500, 200, 100, 50, 20, 10]
x=0
for i in range(6):
 y=notes[i]
 x=int(cash/y)
 cash=int(cash%y)
 print(y, x)
if(cash>0): 
 x=-1