import sys
from collections import deque
# sys.stdin = open('input.txt')

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().split()))+[1])
# 두번째 축의 애들에 번호가 달려. 뒤에 나오는 애들보다 크면.
# max값을 갱신하면서 가면. 100만 괜찮나
# 정렬하면 안된다. 너무 커
# 이해를 잘못했네. 1차원 ------------ 여기에 겹치는 수. 카운팅은 안돼.
lst.sort(key = lambda x:(x[0],x[1]))
deq = deque(lst)
index = 0
max_n = 0
print(lst)
while deq:
    index += 1
    start,end,cnt = deq.popleft()
    if max_n < cnt:
        max_n = cnt
    for i in range(index,N):
        next_start,next_end,cnt = lst[i]
        
        if next_start >= end:
            break
        if start <= next_start <end:
            if end > next_end:
                deq.append([next_start,next_end,cnt+1])
                deq.append([next_end,end,cnt])
            else:
                deq.append([next_start,end,cnt+1])
                deq.append([end,next_end,cnt])

print(max_n)