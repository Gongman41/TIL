            # 배열의 범위를 벗어나지 않고, 방문하지 않았고, 치즈가 아닌 경우에만 탐색합니다.
            if 0 <= lr < N and 0 <= lc < M:
                if visited[lr][lc] == 0 and matrix[lr][lc] == 0:
                    deq.append([lr, lc])
                    visited[lr][lc] = 1
                elif matrix[lr][lc] == 1:
                    # 치즈가 있을 경우 visited 값을 증가시킵니다.
                    visited[lr][lc] = visited[lr][lc] + 1

# 입력을 받습니다.
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우를 탐색하기 위한 방향 배열입니다.
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
