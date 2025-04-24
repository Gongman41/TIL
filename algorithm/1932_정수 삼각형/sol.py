# 백트래킹으로 생각했으나 하다보니 dp였던

import sys
input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n + 1)]

# 초기값 설정 (삼각형 맨 위값)
dp[0][0] = tri[0][0]

# DP 계산 (Bottom-up 방식)
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + tri[i][j]  # 왼쪽 대각선에서 오는 경우
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + tri[i][j]  # 오른쪽 대각선에서 오는 경우
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]  # 두 방향 중 큰 값 선택

# 최대값 출력
print(max(dp[n - 1]))
