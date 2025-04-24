# import sys
# from collections import deque
# input = sys.stdin.readline
# n,m = map(int,input().split())

# matrix = []
# start = []
# for i in range(n):
#     lst = list(map(int,input().split()))
#     matrix.append(lst)
#     if 2 in lst:
#         start.append(i)
#         start.append(lst.index(2))
# # 갱신하면서 가야될거같은데. 다음 목적지가 자기보다 작으면, -1, matrix에서 0이면 멈춤

# result = [[0]*m for _ in range(n)]
# result[start[0]][start[1]] = 0
# q = deque([start])

# while q:
#     x,y = q.popleft()
#     for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
#         nx,ny = x+dx, y+dy
#         if 0<=nx<n and 0<=ny<m and matrix[nx][ny] == 1 and (result[nx][ny] > result[x][y] or result[nx][ny] == 0):
#             result[nx][ny] = result[x][y] + 1
#             q.append([nx,ny])
# for i in range(n):
#     print(*result[i])

# 갱신할 필요없이 방문처리만. 제일 먼저 가는놈이 제일 최단거리임
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

matrix = []
start = None  # 목표 지점 (2)의 위치 저장
for i in range(n):
    lst = list(map(int, input().split()))
    matrix.append(lst)
    if 2 in lst:
        start = (i, lst.index(2))  # 목표 지점 찾기

# 결과 배열 초기화
result = [[-1] * m for _ in range(n)]

# 원래 갈 수 없는 땅(0인 곳)은 결과 배열에서 0으로 설정
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            result[i][j] = 0

# BFS 준비
q = deque([start])
result[start[0]][start[1]] = 0  # 목표 지점의 거리 0

# BFS 수행
while q:
    x, y = q.popleft()
    cur_dist = result[x][y]

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1 and result[nx][ny] == -1:
            result[nx][ny] = cur_dist + 1  # 거리 갱신
            q.append((nx, ny))

# 결과 출력
for row in result:
    print(*row)
