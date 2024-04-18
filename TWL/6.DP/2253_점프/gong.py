# N,M = map(int,input().split())
# n_lst = [1]*(N+1)
# for _ in range(M):
#     n_lst[int(input())] = 0
# i = 1
# while not (i*(i+1)/2 >= N-1 and N-1 > i*(i-1)/2):
#     i+=1
# print(i)



'''
2 1
3 1  4 2
4 1 5 2 5 1 6 2 7 3
'''
# 가는 길 못가는 곳 뺴고. dp에 널뛰기 횟수,널뛰기 거리 저장. 널뛰기 횟수가 작으면 거리도 더 큰가?  널뛰기 횟수 비교해서 적은 놈 거리 저장. 
# 최단거리 갱신..? 
# 크기가 작은 돌은 어떡해
# 테이블 만드는 법. 

from sys import stdin

N, stone_n = map(int, stdin.readline().split())

stone = set()
for _ in range(stone_n):
    stone.add(int(stdin.readline().rstrip()))

dp  = [[10001]* (int((2*N)**0.5)+2)  for _ in range(N+1)]
# int((2*N)**0.5)+2 이건 이해가 안가네. 아 한번에 갈 수 있는 거리 내에. 한번에 뛸 수 있는 게 최소 횟수보단 작아야.
# 넘으면 애초에 갈 수가 없다.

dp[1][0] = 0
for i in range(2, N+1):
    if i in stone:
        continue
    # 작은 돌에는 10001 있음, 다른 거는 거기에 갈 수 있는 애들중에 최솟값 + 1
    for v in range(1,int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1]) +1


ans = min(dp[N])
if ans == 10001:
    print(-1)
else:
    print(ans)