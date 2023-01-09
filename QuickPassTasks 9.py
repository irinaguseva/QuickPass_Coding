# QuickPass 9
from nltk.tokenize import RegexpTokenizer

path = input()
#tokenizer = RegexpTokenizer("[a-z]+(?:-[а-я]+)*")
tokenizer = RegexpTokenizer(r"[A-Za-z]\w+")

para = ''
with open(path, encoding="utf8") as f:
    file = f.readlines()
for line in file:
    line = line.lower().rstrip('\n')
    para += line + ' '

text_without_trash = [w for w in set(tokenizer.tokenize(para)) if not any(c.isdigit() for c in w)]
text_without_trash = sorted(text_without_trash)
text_without_trash = sorted(text_without_trash, key = lambda x : x[-1])
print(*text_without_trash)
