# QuickPassTasks 1
import sys
from math import *

def extra_zeros(n, d=2):
    return f"{n:.{d}f}"

max1 = float('-inf')
max2 = float('-inf')
maxans = float('-inf')
pairs = []
#lst = [[3, 2], [5, 3], [18, 2]]
for line in sys.stdin:
    line = [int(x) for x in line.split()]
    max1 = max(line[0], max1)
    max2 = max(line[1], max2)
    ans = str(extra_zeros(round(line[0]/line[1], 2)))
    maxans = max(maxans, len(ans))
    pairs.append([line[0], line[1], ans])

leng1 = len(str(max1)) + 1
leng2 = len(str(max2)) + 1
for p in pairs:
    init = 0
    print(str(p[0]) + ' '*(leng1- len(str(p[0]))) + ' / ' + str(p[1])
          + ' '*(leng2- len(str(p[1]))) + ' = ' +
          (' '*(maxans-len(p[2]))) + p[2])

