
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    n_list = list(map(int,input().split()))
    max_n = max(n_list)
    min_n = min(n_list)
    print(f"#{test_case} {max_n - min_n}")







