import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = [[1] for i in range(N+1)]
    a[1] = [1]
    if N != 1:
        a[2] = [1,1]

        for n in range(3,N+1):
            for m in range(len(a[n-1])-1):
                a[n].append(a[n-1][m]+a[n-1][m+1])
            a[n].append(1)
    print(f'#{tc}')
    for i in a[1:]:
        print(*i)



