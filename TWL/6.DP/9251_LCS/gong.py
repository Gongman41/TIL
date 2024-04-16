
# num = input()
# num2 = input()
# count = 0
# for i in range(1<<len(num),-1,-1):
#     tem = []
#     for j in range(len(num)):
#         if i &(1<<j):
#             tem.append(num[j])
#     print(i,tem)
#     for n in range(1<<len(num2),-1,-1):
#         tem2 = []
#         for m in range(len(num2)):
#             if n & (1<<m):
#                 tem2.append(num2[m])
#         if tem == tem2:
#             print(tem)
#             count = len(tem)
#             break
#     else:
#         continue
#     break
    
# print(count)        

A = input()
B = input()
dp = [1]*(len(A))

# A = int(input())
# num = list(map(int, input().split()))

# dp = [1] * (A)

# for i in range(1, A):
#     for j in range(i-1, -1, -1):
#         if num[i] > num[j]:
#             dp[i] = max(dp[j] + 1, dp[i])
            
# print(max(dp))

