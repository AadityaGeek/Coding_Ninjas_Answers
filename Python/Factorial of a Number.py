# Author : Aaditya Kumar
# Question : Factorial of a Number
# Question Link : https://www.naukri.com/code360/guided-paths/basics-of-python/content/118790/offering/1461384?leftPanelTab=0

# Solution
#Your code goes here
n = int(input())

if n < 0:
    print("Error")
    
elif n == 0:
    print(1)
    
else:
    i = n
    fact = 1
    
    for i in range(1,n+1):
         fact=fact*i
        
    print(fact)