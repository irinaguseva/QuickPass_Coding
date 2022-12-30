# QuickPass 3
while True:
    x = int(input())
    if not x:
        break
    if x % 100 in range(11,15) or x % 10 in [0,5,6,7,8,9]:
        print(x, 'кроликов')
    elif x % 10 == 1:
        print(x, 'кролик')
    elif x % 10 in [2,3,4]:
        print(x, 'кролика')
