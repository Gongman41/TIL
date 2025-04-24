import sys
input = sys.stdin.readline

N,M = map(int,input().split())
pk_list = [0]
pk_n_list = {}
for n in range(1,N+1):
    name = input().strip()
    pk_list.append(name)
    pk_n_list[name] = n

for _ in range(M):
    target = input().strip()
    if target.isdigit():
        print(pk_list[int(target)])
    else:
        print(pk_n_list[target])