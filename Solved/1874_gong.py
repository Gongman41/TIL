from collections import deque
N = int(input())
target_lst = [int(input()) for _ in range(N)] #메모리 낭비긴 함
target_deq = deque(target_lst)# 위에는 순열 순서, 이거는 없앨 거. 왜 이렇게 했냐.
n_lst = []# deque가 대가리 값 반환하는 메서드가 없는 줄 몰랐음. 이거는 append할 리스트
result = []#결과
j = 0 # target_lst 랑 deq랑 싱크 맞추기용
for n in range(1,N+1):
    
    n_lst.append(n)
    result.append('+')
    while target_deq and n_lst  and target_lst[j] <= n_lst[-1]:
        if target_lst[j] == n_lst[-1]: #리스트 값 있고 타겟이 n와 같다
            target_deq.popleft()
            j += 1# 순열에서 빼고
            
        n_lst.pop()
        result.append('-') #리스트는 while문대로 빼주고
       
    if j != N and  n > target_lst[j] and target_lst[j] not in n_lst:
        result = ['no'] # 다 돌지 않았고 n이 더 큰데 타겟이 작고 이놈이 앞으로 들어올 일이 없을 때
        break
    
for i in range(len(result)):
    print(result[i])