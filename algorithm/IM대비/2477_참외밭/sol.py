import sys
sys.stdin = open('input.txt')
K = int(input())
point_lst = []
start_point = [500,500]
max_x = 0
min_x = 1000
max_y = 0
min_y = 1000
for _ in range(6):
    a,b = map(int,input().split())
    if a == 1:
        start_point[0] += b
        point_lst.append(start_point[:])
    elif a == 2:
        start_point[0] -= b
        point_lst.append(start_point[:])
    elif a == 3:
        start_point[1] -= b
        point_lst.append(start_point[:])
    elif a == 4:
        start_point[1] += b
        point_lst.append(start_point[:])
    max_x = max(max_x, start_point[0])
    min_x = min(min_x, start_point[0])
    max_y = max(max_y, start_point[1])
    min_y = min(min_y, start_point[1])

sm_r = [0,1000]
sm_l = [1000,0]
for p in point_lst:
    if not(p[0] in (min_x,max_x)  and p[1] in (min_y,max_y)):
        if sm_r[0] <= p[0] and sm_r[1] >= p[1]:
            sm_r = p
        if sm_l[0] >= p[0] and sm_l[1] <= p[1]:
            sm_l = p
sm_box = abs((sm_l[0]-sm_r[0])*(sm_l[1]-sm_r[1]))
bg_box = (max_x-min_x)*(max_y-min_y)
print(K*(bg_box-sm_box))






