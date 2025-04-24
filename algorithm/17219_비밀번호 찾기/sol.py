import sys
input = sys.stdin.readline
N,M = map(int,input().split())
dic_lst = {}
for _ in range(N):
    site, password = input().split()
    dic_lst[site] = password

for _ in range(M):
    target = input()
    print(dic_lst[target[:-1]])
    