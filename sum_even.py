n = int(input("Enter Number to calculate sum: "))
sum = 0
for num in range(0, n+1):
 if num%2==0:
  sum = sum+num
print("numbers is: ", sum )