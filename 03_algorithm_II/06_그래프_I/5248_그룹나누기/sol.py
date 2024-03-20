import sys
sys.stdin = open('input.txt')


#
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    tem = list(map(int,input().split()))
    n_lst = [i for i in range(N+1)]
    rank = [0]*(N+1)
    cnt = 0
    for m in range(0,M*2,2):
        n_lst[tem[m+1]] = tem[m]
        rank[tem[m+1]] += 1
    for j in range(1,N+1):
        if n_lst[j] == j:
            cnt +=1

    print(f'#{tc} {cnt}')


