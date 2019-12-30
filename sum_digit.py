#sum of digits in a number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    d = num%10
    num = num//10
    sum += d
print("The sum of digits of number is",sum)