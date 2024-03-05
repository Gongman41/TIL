from collections import deque
N = int(input())
target_lst = [int(input()) for _ in range(N)]
target_deq = deque(target_lst)
n_lst = []
result = []
j = 0
for n in range(1,N+1):
    
    n_lst.append(n)
    result.append('+')
    while target_deq and n_lst  and target_lst[j] <= n_lst[-1]:
        if target_lst[j] == n_lst[-1]:
            target_deq.popleft()
            j += 1
            
        n_lst.pop()
        result.append('-')
       
    if j != N and  n > target_lst[j] and target_lst[j] not in n_lst:
        result = ['no']
        break
    
for i in range(len(result)):
    print(result[i])