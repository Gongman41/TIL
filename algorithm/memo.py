used = [False, False, False,False,False,False,False] #브랜치 개수
path = []

def KFC(x):
    if x == 2:
        print(path)
        return
    for i in range(1,7):
        if used[i] == True:continue
        used[i] = True
        path.append(i)
        KFC(x+1)
        path.pop()
        used[i] = False
KFC(0)