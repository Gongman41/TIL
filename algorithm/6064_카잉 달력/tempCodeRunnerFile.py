# 최소 공배수
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M,N,x,y = map(int,input().split())
    cnt = x
    while cnt <= M * N:
        if (cnt - x)% M == 0 and (cnt - y) % N == 0:
            break
        if (cnt - y) % N == 0:
            break
        cnt += M
        
    if cnt >= M * N:
        print(-1)
    else:
        print(cnt)
        
        