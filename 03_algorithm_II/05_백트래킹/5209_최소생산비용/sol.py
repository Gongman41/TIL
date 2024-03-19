import sys
sys.stdin = open('input.txt')

def Searching(n,h,cost):
    global min_cost
    if h == n:
        min_cost = min(cost,min_cost)
        return
    if cost > min_cost:
        return

    for i in range(n):
        if i not in no_lst:
            no_lst.append(i)
            Searching(n,h+1,cost+matrix[h][i])
            no_lst.pop()



T = int(input())
for tc in range(1,T+1):
    N  =int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    min_cost = 10e10
    no_lst = []
    Searching(N,0,0)
    print(f'${tc} {min_cost}')