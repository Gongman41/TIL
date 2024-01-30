T = int(input())

for test_case in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    n_list = list(map(int, input().split()))

    temp = []

    for i in range(len(n_list) - M + 1):
        sum_n = 0
        for m in range(M):
            sum_n += n_list[i + m]
        temp.append(sum_n)

    print(f'#{test_case} {max(temp) - min(temp)}')