T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    number_list = []
    real_total_kill = 0
    total_kill= 0
   
    for n in range(N):
        number_list.append(list(map(int,input().split())))
    for i in range(N):
        for j in range(N):
            for k in range(1-M,M):
                if 0 <= i + k < N:
                    total_kill += number_list[i+k][j]
                if 0 <= j + k < N:
                    total_kill += number_list[i][j+k]
                total_kill -= number_list[i][j]
            real_total_kill = max(real_total_kill,total_kill)
            total_kill= 0
            for k in range(1-M,M):
                if 0 <= i + k < N and 0 <= j+k < N:
                    total_kill += number_list[i+k][j+k]
                if 0 <= i - k < N and 0 <= j+k < N:
                    total_kill += number_list[i-k][j+k]
                total_kill -= number_list[i][j]
            real_total_kill = max(real_total_kill,total_kill)
            total_kill= 0

                
    print(f'#{test_case}')
    print(real_total_kill)
            