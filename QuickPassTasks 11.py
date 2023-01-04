# QuickPassTasks 11
import os

dr = input()
files = os.listdir(dr)

file_for_answer = input()
ans = open(file_for_answer, 'w')

for name in files:
    
    path = dr + '/' + name
    with open(path, 'r') as f:
        file = f.readlines()
    lines = len(file)
    syms = 0
    words = 0
    
    for line in file:   
        line = line.rstrip('\n')
        syms += len(line)
        
        line = line.split()
        words += len(line)
    
    ans.write('|************' + name + '************|\n')
    ans.write('Количество символов: ' + str(syms) + '\n')
    ans.write('Количество слов: ' + str(words) + '\n')
    ans.write('Количество строк: ' + str(lines) + '\n')
ans.close()









