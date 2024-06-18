# Author : Aaditya Kumar
# Question : Fahrenheit to Celsius
# Question Link : https://www.naukri.com/code360/guided-paths/basics-of-python/content/118790/offering/1461384?leftPanelTab=0

# Solution
from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
s=int(input())
e=int(input())
w=int(input())

for i in range(s,e+1,w):
    c=(i-32)*5/9
    c=int(c)

    print(i,c)