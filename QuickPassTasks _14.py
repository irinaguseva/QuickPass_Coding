# QuickPassTasks 14

from nltk.tokenize import RegexpTokenizer

path = input()
tokenizer = RegexpTokenizer("[а-я]+(?:-[a-z]+)*")
para = ''
with open(path, encoding="utf8") as f:
    file = f.readlines()

for line in file:
    line = line.lower().rstrip('\n')
    para += line + ' '
    
text_without_trash = tokenizer.tokenize(para)
total = len(text_without_trash)
unique = len(set(text_without_trash))

print('Лексическое разнообразие =', unique / total) 

