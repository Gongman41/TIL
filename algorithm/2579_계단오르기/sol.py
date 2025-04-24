import sys
input = sys.stdin.readline
n = int(input())

scores = [0] + [int(input().strip()) for _ in range(n)]  # 1-based index

# 예외 처리
if n == 1:
    print(scores[1])
    exit()

# DP 테이블 초기화
dp = [0] * (n + 1)
dp[1] = scores[1]
dp[2] = scores[1] + scores[2] if n > 1 else scores[1]

# DP 점화식 적용
for i in range(3, n + 1):
    dp[i] = max(dp[i-2], dp[i-3] + scores[i-1]) + scores[i]

print(dp[n])  # 마지막 계단까지 도달했을 때의 최대 점수
