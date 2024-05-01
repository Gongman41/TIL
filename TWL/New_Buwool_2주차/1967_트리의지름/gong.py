import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
nodes = [[] for _ in range(n+1)]
max_n = 0
start = 0
for _ in range(n-1):
    par,chd,leng = map(int,input().split())
    nodes[par].append([chd,leng])
    nodes[chd].append([par,leng])
deq = deque([[1,0]])
while deq:
    node,total_len = deq.popleft()
    if max_n <= total_len:
        max_n = total_len
        start = node
    if nodes[node]:
        for next,next_len in nodes[node]:
            deq.append([next,total_len+next_len])
deq.append([start,max_n])
while deq:
    node,total_len = deq.popleft()
    rightmax_n = max(total_len,rightmax_n)
    if nodes[node]:
        for next in nodes[node]:
            deq.append([next,total_len+lengthes[next]])
print(rightmax_n+leftmax_n)
    

    
    