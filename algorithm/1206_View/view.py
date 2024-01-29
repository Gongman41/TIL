
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n_list = list(map(int,input().split()))
    count = 0
    for n in range(2,len(n_list)-2):
        if (n_list[n] - max([s] - max([n_list[n-2],n_list[n-1],n_list[n+1],n_list[n+2]]))

    print(f'#{test_case} {count}')

