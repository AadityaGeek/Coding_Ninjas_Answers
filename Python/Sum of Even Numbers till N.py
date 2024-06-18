# Author : Aaditya Kumar
# Question : Sum of Even Numbers till N
# Question Link : https://www.naukri.com/code360/guided-paths/basics-of-python/content/118790/offering/1461384?leftPanelTab=0

# Solution
#Your code goes here
n=int(input())
sm=0
for i in range(0,n+1):
    
    if(i % 2 == 0):
        sm += i

#print the value of sum.        
print(sm)