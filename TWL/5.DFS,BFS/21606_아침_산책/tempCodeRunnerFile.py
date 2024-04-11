import sys
from collections import deque
# 기본 트리, 시작점과 끝 점은 실내. 이외에는 실외.
N = int(input())
A = input()
Node = [0]
for i in range(N):
    Node.append(int(A[i]))
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent,child = map(int,sys.stdin.readline().split())
    if not tree[child]:
        tree[child].append(parent)
    tree[parent].append(child)
# 모든 정점에서 탐색. 시작점에 실내인 경우에 탐색. 실내일때 끝
deq = deque([])
cnt = 0
for i in range(1,N+1):
    if Node[i] == 1:
        deq.append([i,0])
        while deq:
            cur,last = deq.popleft()
            for t in tree[cur]:
                if t == last:
                    continue
                if Node[t] == 0:
                    deq.append([t,i])
                else:
                    cnt+=1
print(cnt)
        
        
    


    
