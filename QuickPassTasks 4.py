# QuickPassTasks 4
import random
x = random.randint(1, 1024)
k = 10
found = False

while k:
    guess = int(input())
    if guess in range(1, 1024):
        if guess == x:
            found = True
            break
        elif guess < x:
            print('No :( Try something bigger!')
        elif guess > x:
            print('No :( Try something smaller!')  
        k -= 1
    else:
        print('Your input is incorrect. Give me the number from [1, 1024]')

if not found:
    print('GAME OVER!')
else:
    print('YOU WON! IT WAS REALLY', x)

'''   
 10 попыток достаточно, ведь 2^10 = 1024.
 Нужно начать с 512, а далее проверять числа посередине проверяемых интервалов.
 Например, узнав, что 512 слишком большое число, мы понимаем, что
 диапазон поиска сокращается до (1, 512). Далее мы снова выберем число ровно
 посередине диапазона, сократив его в два раза. Максимальное число попыток
 угадать загаданное число составляет log{2}(x), где x - верхняя граница диапазона,
 из которого нужно было выбрать и загадать число.
'''  
