T =int(input())
for tc in range(1,T+1):
    N,K = tuple(map(int,input().split()))
    matrix = [0]*N
    count = 0
    for n in range(N):
        matrix[n] = list(map(int,input().split()))
    for i in range(N):
        th_seq_ = 0
        th_seqI = 0
        for j in range(N):
            if matrix[j][i] == 1:
                th_seq_ +=1
                if j == N-1 and th_seq_ == K:
                    count += 1
            else:
                if th_seq_ == K:

                    count += 1
                th_seq_ = 0

            if matrix[i][j] == 1:
                th_seqI +=1
                if j == N-1 and th_seqI == K:
                    count += 1
            else:
                if th_seqI == K:

                    count += 1
                th_seqI = 0
    print(f'#{tc} {count}')



