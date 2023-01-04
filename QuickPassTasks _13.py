# QuickPassTasks 13
d = {}

while True:
    try:
        line = input().split()
        
        if line[0] == 'DEPOSIT':
            if line[1] not in d:
                d[line[1]] = 0
            d[line[1]] += int(line[2])
            
        elif line[0] == 'WITHDRAW':
            if line[1] not in d:
                d[line[1]] = 0
            d[line[1]] -= int(line[2])            

        elif line[0] == 'BALANCE':
            if line[1] not in d:
                print('ERROR')
            else:
                print(d[line[1]])
                
        elif line[0] == 'TRANSFER':
            if line[1] not in d:
                d[line[1]] = 0
            if line[2] not in d:
                d[line[2]] = 0
            d[line[1]] -= int(line[3])
            d[line[2]] += int(line[3])
                   
        elif line[0] == 'INCOME':
            p = int(line[1])
            for name in d:
                if d[name] > 0:
                    d[name] += int(d[name]*(p/100))
            
    except:
        break
