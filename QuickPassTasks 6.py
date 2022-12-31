# QuickPassTasks - 6
import sys
def f():
    lst = []
    for num in sys.stdin:
        num = int(num)
        lst.append(num**2)
    print(lst)
f()
