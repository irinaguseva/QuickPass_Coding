# QuickPassTasks 5
lst = [str(x) for x in input().split()]
s1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
s2 = 'абвгдежзийклмнопрстуфхцчшщъыьэюяѐ'
dic = {}
dicmir = {}

for i in range(len(s1)):
    dic[s1[i]] = s2[i]
    dicmir[s2[i]] = s1[i]
    
new = []
for i in range(len(lst)):
    word = ''
    for x in lst[i]:
        word += dic[x]
    new.append(word)
    
new.sort()
ans = []
for item in new:
    word = ''
    for x in item:
        word += dicmir[x]
    ans.append(word)
print(*ans)






        
