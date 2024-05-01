import sys
from collections import deque
def BFS(row,col):
    deq = deque([[row,col]])
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    visited[row][col] = 1
    while deq:
        r,c = deq.popleft()
        cnt += 1
        for i in range(4):
            lr = dr[i]+r
            lc = dc[i]+c
            if 0 <= lr < N and 0 <= lc < M and matrix[lr][lc] == '0' and visited[lr][lc] == 0:
                visited[lr][lc] = 1
                deq.append([lr,lc])
        print(cnt)
    return cnt
                

N,M = map(int,input().split())
matrix = [sys.stdin.readline() for _ in range(N)]
result = [[0]*M for _ in range(N)]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '1':
            result[i][j] = BFS(i,j)%10
for i in range(N):
    print(result[i])