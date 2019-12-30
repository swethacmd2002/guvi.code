#product of digits in a number
n = int(input("Enter a number: "))
product = 1
while n > 0:
  product = product * (n % 10) 
  n = n // 10
    
print("The sum of digits of number is",product)