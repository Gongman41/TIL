import sys
sys.stdin = open('input.txt')

def counting_time(start,lst):
    global cnt
    temp = cnt
    for l in range(len(lst)):
        if start <= lst[l][0]:
            start = lst[l][1]
            lst = lst[l:]
            cnt += 1
            break
    if cnt == temp:
        return
    counting_time(start,lst)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    time_lst = [list(map(int,input().split())) for _ in range(N)]
    time_lst.sort(key = lambda  x : x[1])
    cnt = 0
    counting_time(0, time_lst)


    print(f'#{tc} {cnt}')





    # max_n = 0
    # for t in range(N):
    #     tem_lst = [[time_lst[t][0],time_lst[t][1]]]
    #     for i in range(t+1,N):
    #         for tt in tem_lst:
    #             if tt == time_lst[i] or tt[0] < time_lst[i][0] < tt[1] or tt[0] < time_lst[i][1] < tt[1] or (tt[0] <= time_lst[i][0] <= tt[1] and tt[0] <= time_lst[i][1] <= tt[1]):
    #                 break
    #             tem_lst.append(time_lst[i])
    #
    #     max_n = max(max_n,len(tem_lst))
    #
    # print(max_n)


