import sys
input = sys.stdin.readline

N,M = map(int,input().split())
pk_list = [0]
pk_n_list = {}
for n in range(N):
    name = input().strip()
    pk_list.append(name)
    pk_n_list[name] = n

for _ in range(M):
    target = input().strip()
    if target.isdifit():
        print(pk_list[int(target)])
    else:
        print(pk_n_list[target])