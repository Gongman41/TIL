T = 10
for test_case in range(1,T+1):

    N = int(input())
    a = [0]*101
    n_list = list(map(int,input().split()))
    max_n = 0
    min_n = 0
    for n in n_list:
        a[n] += 1
    print(a)
    for i in range(100,-1,-1):
        if i == 0:
            pass
        while a[i] != 0 and N != 0:
            a[i] -= 1
            a[i-1] += 1
            N -= 1
            for j in range(101):
                if a[j] != 0:
                   a[j] -= 1
                   a[j+1] += 1
                   break
        if N == 0:
            max_n = i
            break

    for j in range(101):
        if a[j] != 0:
            min_n = j
            break
    print(max_n,min_n,N)
    print(f'#{test_case} {max_n - min_n}')


