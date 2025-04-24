import sys

input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 4방향 이동 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부 체크
visited = [[False] * M for _ in range(N)]

# 최대값 저장 변수
max_value = max(map(max, board))  # 가장 큰 블록 값
result = 0  # 최댓값 저장

# DFS로 4칸까지 탐색하는 함수
def dfs(x, y, depth, total):
    global result

    # 4칸 탐색 완료 시 최댓값 갱신
    if depth == 4:
        result = max(result, total)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 범위 체크 및 방문 여부 확인
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False  # 백트래킹

# 'ㅗ', 'ㅜ', 'ㅓ', 'ㅏ' 모양을 위한 별도 함수
def check_special_shape(x, y):
    global result
    # ㅗ, ㅜ, ㅓ, ㅏ 모양 체크
    for shape in [
        [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅗ
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
        [(0, 0), (0, 1), (0, 2), (-1, 1)], # ㅜ
        [(0, 0), (1, 0), (2, 0), (1, -1)]  # ㅓ
    ]:
        try:
            total = sum(board[x + dx][y + dy] for dx, dy in shape)
            result = max(result, total)
        except IndexError:
            continue

# 모든 위치에서 DFS 및 특수 모양 검사
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_special_shape(i, j)

# 결과 출력
print(result)
