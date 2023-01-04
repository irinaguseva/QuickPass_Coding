# QuickPassTasks 12

def mat_add(m1, m2):
    new = [[0 for x in range(len(m1[0]))] for x in range(len(m1))]
    for j in range(len(m1)):
        for i in range(len(m1[0])):
            new[j][i] = m1[j][i] + m2[j][i]
    return new

m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
m2 = [[-1, -2, -3],
      [-4, -5, -6],
      [-7, -8, -9]]
print(mat_add(m1, m2))
