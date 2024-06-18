# Author : Aaditya Kumar
# Question : Find power of a number
# Question Link : https://www.naukri.com/code360/guided-paths/basics-of-python/content/118790/offering/1461384?leftPanelTab=0

# Solution
from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
x,n = map(int,input().split())

ans = 1

while n > 0:
    
    ans *= x
    
    n -= 1
    
print(ans)