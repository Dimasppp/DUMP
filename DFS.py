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

passed = []
YCounter = 0

def dfs(now):
    if now not in passed:
        passed.append(now)
        for i in nodeAll[now]:
            dfs(i)

dfs('X')