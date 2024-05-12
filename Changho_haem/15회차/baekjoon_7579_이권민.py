N,M = map(int,input().split())
memories = [0] + list(map(int,input().split()))
costs = [0] + list(map(int,input().split()))
length = sum(costs)+1
dp = [[0]*(length) for _ in range(N+1)]
result = 10e10

for i in range(1,N+1):
    cost,memory = costs[i], memories[i]
    for j in range(length):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost]+memory, dp[i-1][j])
        if M <= dp[i][j]:
            result = min(result,j)
print(result)
        