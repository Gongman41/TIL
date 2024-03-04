'''
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
'''
def checking(r,c,color):
    global max_n
    r_n = 1
    c_n = 1
    up_r,do_r,l_c,r_c = 1,1,1,1
    while r+up_r != N:
        if color == matrix[r+up_r][c]:
            r_n += 1
            up_r +=1
        else: 
            break
    while r-do_r != -1:
        if color == matrix[r-do_r][c]:
            r_n += 1
            do_r +=1
        else: 
            break
    while c+r_c != N:
        if color == matrix[r][c+r_c]:
            c_n += 1
            r_c +=1
        else: 
            break
    while c-l_c !=-1:
        if color == matrix[r][c-l_c]:
            c_n += 1
            l_c +=1
        else: 
            break
    max_n = max(max_n,r_n,c_n)
    
N = int(input())
matrix = [list(input()) for _ in range(N)]
dr = [1,0,-1,0,0]
dc = [0,-1,0,1,0]
max_n = 1
if N >= 3:
    for i in range(N):
        for j in range(N):
            for m in range(5):
                lr = i+dr[m]
                lc = j+dc[m]
                if 0 <= lr < N and 0 <= lc < N and (i,j == lr,lc or matrix[i][j] != matrix[lr][lc]):
                    matrix[i][j],matrix[lr][lc] = matrix[lr][lc],matrix[i][j]
                    checking(i,j,matrix[i][j])
                    matrix[i][j],matrix[lr][lc] = matrix[lr][lc],matrix[i][j]
    print(max_n)
else:
    for i in range(N):
        for j in range(N):
            for m in range(4):
                lr = i+dr[m]
                lc = j+dc[m]
                if 0 <= lr < N and 0 <= lc < N and  matrix[i][j] != matrix[lr][lc]:
                    matrix[i][j],matrix[lr][lc] = matrix[lr][lc],matrix[i][j]
                    checking(i,j,matrix[i][j])
                    matrix[i][j],matrix[lr][lc] = matrix[lr][lc],matrix[i][j]
    print(max_n)
# 행 열 단위로 바꾸는 경우의 수 다 체크. 2-3가지로 시작.깊이는 N-i 브랜치는 3, 종료조건은 같지 않을 때