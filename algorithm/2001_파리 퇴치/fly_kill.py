import sys
sys.stdin = open("input.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    n_list = []
    real_total_kill = 0

    for n in range(N):
        n_list.append(list(map(int, input().split())))
    for i in range(N - M + 1): #위치별로 오,아래 범위를 킬
        for j in range(N - M + 1):
            total_kill = 0 # 이번 위치에서 죽인 파리들
            for k1 in range(M):
                for k2 in range(M):
                    total_kill += n_list[i + k1][j + k2]
            real_total_kill = max(total_kill, real_total_kill) #점수 갱신

    print(f'#{test_case} {real_total_kill}')