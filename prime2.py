# Python program to print all prime numbers from 1 to n
   
n = int(input("Enter n: "))  

for n in range(1,n):  
   if n > 1:  
       for i in range(2,n):  
           if (n % i) == 0:  
               break  
       else:  
           print(n)  