def check(x1,x2,y1,y2):
    global blue
    global white
    if x2-x1 == 1:
        return
    for i in range(x1,x2+1):
        for j in (y1,y2+1):
            if not matrix[i][j]:
                check(x1,x2//2+1,y1,y2//2+1)
                check(x2//2+1, x2, y1, y2 // 2 + 1)
                check(x2//2+1, x2 // 2 + 1, y2//2+1, y2)
                check(x1, x2 // 2 + 1, y2 // 2 + 1,y2)


                break


N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]