# program to find first and last digits of a number 
  
# Find the first digit 
def firstDigit(n) : 
  while n >= 10:  
        n = n / 10; 
  return int(n) 
  
# Find the last digit 
def lastDigit(n) : 
  return (n % 10) 
n = int(input())
print(firstDigit(n), end = " ")  
print(lastDigit(n))
