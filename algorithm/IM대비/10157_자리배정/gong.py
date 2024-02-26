import sys
sys.stdin = open('input.txt')
C,R = map(int,input().split())
K = int(input())
visited = [[0]*C for _ in range(R)]
cnt = 1
dr = [0,1,0,-1]
dc = [1,0,-1,0]
r,c = 0,0
go_r = 1
go_c = 0
while True:
    cnt += 1
    can_cnt = 0
    tem_r = 0
    tem_c = 0
    visited[r,c] = 1

    for n in range(4):
        lr = r+dr[n]
        lc = c+lc[n]
        if 0 <= lr < R and 0 <= lc < C and visited[lr][lc] == 0:
            can_cnt +=1
            tem_r = lr
            tem_c = lc
    if can_cnt == 1:
        go_r = tem_r
        go_c = tem_c
    elif can_cnt == 0:
        break
    r += go_r
    c += go_c







