A = int(input())
num = input()

dp = [1] * (A)

for i in range(1, A):
    for j in range(i-1, -1, -1):
        if num[ord(i)] > num[ord(j)]:
            dp[i] = max(dp[j] + 1, dp[i])
            
print(max(dp))