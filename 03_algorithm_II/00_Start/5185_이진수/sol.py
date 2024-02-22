import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,N_16 = map(str,input().split())
    result = bin(int(N_16,16))[2:].zfill(int(N)*4)
    print(f'#{tc} {result}')
