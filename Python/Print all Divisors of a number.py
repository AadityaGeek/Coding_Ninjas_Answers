# Author : Aaditya Kumar
# Question : Print all Divisors of a number
# Question Link : https://www.naukri.com/code360/guided-paths/basics-of-python/content/118790/offering/1461384?leftPanelTab=0

# Solution
from typing import List

def printDivisors(n: int) -> List[int]:
    divisiors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisiors.append(i)
            if n//i!=i:
                divisiors.append(n//i)

    divisiors.sort()
    return divisiors