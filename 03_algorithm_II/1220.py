T = 10
for tc in range(1,T+1):
    N = int(input())
    n_lst = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        check = 0
        for i in range(N):
            if check%2 == 0:
                if n_lst[i][j] == 1:
                    check += 1
            else:
                if n_lst[i][j] == 2:
                    check += 1
        cnt = check//2
    print(f'#{tc} {cnt}')

