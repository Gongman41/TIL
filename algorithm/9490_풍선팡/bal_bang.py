import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    real_fl_count = 0
    fl_list = []
    for _ in range(N):
        fl_list.append(list(map(int,input().split())))
    for i in range(N):
        for j in range(M):
            fl_count = 0
            fl_fl_count = 0
            fl_fl_count = fl_list[i][j] #해당 인덱스가 리스트에 없을 때
            for f in range(fl_fl_count):
                if i - 1 -f >= 0:
                    fl_count += fl_list[i-1 - f][j]

                if i+1+f <= N-1 :
                    fl_count += fl_list[i +1+f][j]

                if j - 1-f >= 0:
                    fl_count += fl_list[i][j-1-f]

                if j + 1+f <= M - 1:
                    fl_count += fl_list[i][j+1+f]
            fl_count += fl_fl_count
            real_fl_count = max(real_fl_count,fl_count)
    print(f'#{tc} {real_fl_count}')

