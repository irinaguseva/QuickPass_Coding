# QuickPassTasks 7
def applier(lst, method):
    for i in range(len(lst)):
        lst[i] = getattr(lst[i], method)()
    return lst
lst = input().split()
method = input() 
print(applier(lst, method))


