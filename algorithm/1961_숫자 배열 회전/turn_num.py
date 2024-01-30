T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [0]*N
    for i in range(N):
        matrix[i] = list(map(int,input().split()))
    print(f'#{tc}')
    for le in range(N):
        a,b,c = '','',''
        for li in range(N):
            a += str(matrix[N-1-li][le])
            b += str(matrix[N-1-le][N-1-li])
            c += str(matrix[li][N-1-le])
        print(f'{a} {b} {c}')


