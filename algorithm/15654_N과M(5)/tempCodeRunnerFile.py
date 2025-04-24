from itertools import combinations

N,M = map(int,input().split())
n_lst = sorted(list(map(int,input().split())))
for i in combinations(n_lst,M):
    print(" ".join(map(str,i)))
