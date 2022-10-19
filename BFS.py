nodeAll = {
    'X' : ['A1','B2'],
    'A1': ['B1','C'],
    'C' : ['Y2'],
    'Y2': [],
    'B1': ['D1','Y1'],
    'D1': [],
    'Y1': [],
    'B2': ['A2','Y3'],
    'Y3': [],
    'A2': ['D2','E'],
    'D2': [],
    'E' : ['Y4'],
    'Y4': []
}

passed = ['X']
checker = ['X']
YCounter = 0

while checker:
    willpassed = checker.pop(0)
    for i in nodeAll[willpassed]:
        if i not in passed:
            checker.append(i)
            passed.append(i)
        else:
            break

for i in passed:
    if 'Y' in i:
        YCounter += 1
    else:
        pass

print(checker)
print(passed)
print(YCounter)