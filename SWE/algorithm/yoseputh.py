N,K = tuple(map(int,input().split()))
n_list = list(range(1,N+1))
osp = []
current = K-1
for i in range(N):

    while current >= len(n_list):
        current -= len(n_list)
    osp.append(n_list.pop(current))
    current += K - 1
print(f"<{', '.join(map(str, osp))}>")
