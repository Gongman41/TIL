import sys
n,k = map(int,input().split())
coin_lst = []
for _ in range(n):
    coin_lst.append(int(sys.stdin.readline()))

dp = [0]*(k+1)
for j in range(1,k+1):
    for i in range(n):
        if coin_lst[i] <= j:
            dp[j] = max(dp[j-coin_lst[i]] +1,dp[j])
print(dp[k])