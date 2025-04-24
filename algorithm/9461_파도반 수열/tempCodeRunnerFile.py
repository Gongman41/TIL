T = int(input())
n_lst = [0]*101
n_lst[1] = 1
n_lst[2] = 1
n_lst[3] = 1
for i in range(4,101):
    n_lst[i] = n_lst[i-3] + n_lst[i-2]
print(n_lst)
for _ in range(T):
    N = int(input())
    print(n_lst[N])
    