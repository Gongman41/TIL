# 시작위치, visited
from collections import deque
import sys

N,M = map(int,input().split())
matrix = []
visited = [[0]*M for _ in range(N)]
st_xy = []
cnt = 0
for i in range(N):
    matrix.append(input())
    for j in range(M):
        if matrix[i][j] == 'I':
            st_xy = [i,j]

q = deque([st_xy])
visited[st_xy[0]][st_xy[1]] = 1
while q:
    x, y = q.popleft()
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] != 'X' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            q.append([nx,ny])
            if matrix[nx][ny] == 'P':
                cnt += 1

if cnt == 0:
    print('TT')
else:
    print(cnt)