# Author : Aaditya Kumar
# Question : Set Bits
# Question Link : https://www.naukri.com/code360/guided-paths/basics-of-python/content/118790/offering/1461384?leftPanelTab=0

# Solution
from os import *
from sys import *
from collections import *
from math import *


#Write your countBits function here.
def countBits(n):
    count = 0
    while n:
        count += n & 1  # Check the least significant bit (LSB)
        n >>= 1          # Right shift n by 1 bit (divide by 2)
    return count
     
n = int(input())
print(countBits(n))