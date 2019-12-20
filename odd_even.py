odd[]
even[]
n=[int(n) for n in input("enter the values: ").split()]
print("number of list is: ",x)
for i in n:
 if(i%2==0):
  even.append(i)
else:
  odd.append(i)
print(even)
print(odd)
print("sum of the element in odd list :" sum (odd))
print("sum of the element in even list :"sum (even))