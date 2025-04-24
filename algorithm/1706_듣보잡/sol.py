import sys
input = sys.stdin.readline

N,M = map(int,input().split())
see_lst = {}
sl_lst = []
for _ in range(N):
    see_lst[input().strip()] = 1
for _ in range(M):
    l = input().strip()
    if l in see_lst:
        sl_lst.append(l)
sl_lst.sort()
print(len(sl_lst))
for s in sl_lst:
    print(s)
        

