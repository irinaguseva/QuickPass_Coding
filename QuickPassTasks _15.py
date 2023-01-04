# QuickPassTasks 15

from nltk.tokenize import RegexpTokenizer

# path = 'sky.txt'
path = input()
tokenizer = RegexpTokenizer("[а-я]+(?:-[a-z]+)*")
para = ''
with open(path, encoding="utf8") as f:
    file = f.readlines()

for line in file:
    line = line.lower().rstrip('\n')
    para += line + ' '
    
text_without_trash = tokenizer.tokenize(para)
d = {}
for w in text_without_trash:
    if w not in d:
        d[w] = 0
    d[w] += 1
d = sorted(d.items(), key = lambda x : -x[1])
i = min(10, len(d))
for j in range(i):
    print(d[j][0], d[j][1])

