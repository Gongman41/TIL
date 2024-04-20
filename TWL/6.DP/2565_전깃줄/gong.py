A = [[0,0]]
n = int(input())
for _ in range(n):
    i,j = map(int,input().split())
    A.append([i,j])
A.sort()
dp = [1]*(n+1)
for i in range(2,n+1):
    for j in range(1,i):
        if A[i][1] > A[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
                    
print(n - max(dp))
                
        
# 겹치는 애들 선택적으로 뺴면서 가면 될거같기도.
# 카운트 따로. 갱신된 B의 값을 dp로
# 순조롭게 되는 놈들만 저장


            