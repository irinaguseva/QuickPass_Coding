# QuickPassTasks 10

path1 = input()
codecs1 = input()
path2 = input()
codecs2 = input()

with open(path1, encoding=codecs1) as f:
    data = f.read()
    
data = data.encode()
data = data.decode(codecs2, errors='ignore')

with open(path2, 'w', encoding=codecs2) as f:
    f.write(data)
