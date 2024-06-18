# Author : Aaditya Kumar
# Question : Swap Two Numbers
# Question Link : https://www.naukri.com/code360/guided-paths/basics-of-python/content/118790/offering/1461384?leftPanelTab=0

# Solution
from typing import List

def swapNumber(a:list,  b: list) -> None:
    # write your code here
    a[0] = a[0] + b[0]
    b[0] = a[0] - b[0]
    a[0] = a[0] - b[0]