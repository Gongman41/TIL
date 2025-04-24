import sys

n = int(sys.stdin.readline().strip())

# DP 테이블 생성
dp = [0] * (n + 1)
dp[1] = 1
if n > 1:
    dp[2] = 3

# DP 점화식 적용
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007

print(dp[n])
