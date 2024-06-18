# Author : Aaditya Kumar
# Question : Calculate Simple Interest
# Question Link : https://www.naukri.com/code360/guided-paths/basics-of-python/content/118790/offering/1461384?leftPanelTab=0

# Solution
from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
principal = int(input())
rate = float(input())

time = int(input())

#calculating the si using mathematical formula si = (p * r * t) / 100
si = int((principal * rate * time) / 100)


print(si)