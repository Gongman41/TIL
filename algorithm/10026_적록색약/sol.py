import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
mat = [input() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == True:
            continue
        cnt += 1
        color = mat[i][j]
        q = deque([[i,j]])
        visited[i][j] = True
        while q:
            r,c = q.popleft()
            for nr,nc in [(-1,0),(1,0),(0,1),(0,-1)]:
                lr,lc = r+nr, c+nc
                if 0 <= lr < N and 0 <= lc < N and not visited[lr][lc] and mat[lr][lc] == color:
                    q.append((lr,lc))
                    visited[lr][lc] = True
                  

visited = [[0]*N for _ in range(N)]
r_cnt = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == True:
            continue
        if mat[i][j] in ['R','G']:
            color = ['R','G']
        else:
            color = ['B']
        r_cnt += 1
        q = deque([[i,j]])
        visited[i][j] = True
        while q:
            r,c = q.popleft()
            for nr,nc in [(-1,0),(1,0),(0,1),(0,-1)]:
                lr,lc = r+nr, c+nc
                if 0 <= lr < N and 0 <= lc < N and not visited[lr][lc] and mat[lr][lc] in color:
                    q.append((lr,lc))
                    visited[lr][lc] = True

print(cnt,r_cnt)