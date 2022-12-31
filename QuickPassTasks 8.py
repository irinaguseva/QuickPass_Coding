counter = 0

def fib(a, b, k):
    global counter
    counter += 1
    if k == 0:
        return b
    else:
        return fib(a+b, a, k-1)
    
n = int(input())
print('Номер числа:', n)
print('Число:', fib(1, 0, n))
print('Количество вызовов функции:', counter)
