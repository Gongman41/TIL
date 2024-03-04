N = int(input())
n_lst = list(map(int,input().split()))
n_lst.sort()
result = 0
for n in range(N,0,-1):
    result += n_lst[N-n]*n
print(result)
