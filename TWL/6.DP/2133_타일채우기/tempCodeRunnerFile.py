N = int(input())
dp = [0]*(N+1)
dp[0] = 1
dp[2] = 3
if N%2 == 1:
    print(0)
else:
    for i in range(4,N+1,2):
        dp[i] = dp[i-2]*3+2
    print(dp[N])