import math

N = int(input())
1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 4, 2,
# N 에 루트를 씌우고 정수값 추출.0이 될 때까지.

# cur_n = N
# cnt = 0
# while cur_n:
#     num = int(cur_n**(1/2))
#     cur_n -= num**2
#     cnt += 1
#     print(cur_n,num)

# print(cnt)
    
dp = [float('inf')] * (N + 1)
dp[0] = 0  # 0은 제곱수 합으로 표현할 필요 없음

for i in range(1, N + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[N])