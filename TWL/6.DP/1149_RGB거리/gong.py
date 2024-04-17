import sys
N = int(input())
n_lst = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
n_color = [[1000001]*3 for _ in range(N)]
n_color[0] = n_lst[0]
for i in range(1,N):
    for j in range(3):
        n_color[i][j] = min(n_color[i-1][(j+1)%3]+n_lst[i][j],n_color[i-1][(j+2)%3]+n_lst[i][j],n_color[i][j])
print(min(n_color[N-1]))
