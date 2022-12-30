# QuickPassTasks 2
from math import *

n = 0
s1, s2 = 0, 0

while True:
    x = int(input())
    if not x:
        break
    n += 1
    s1 += x
    s2 += x*x
    
s = s1 / n
st_dev = sqrt((s2+s*s*n-2*s1*s)/(n - 1))
print(st_dev)   
