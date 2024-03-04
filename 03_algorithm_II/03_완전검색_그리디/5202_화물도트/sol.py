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



'''
for idx in range(int(input())):
    schedule = [tuple(map(int,input().split())) for _ in range(int(input()))]
    schedule.sort(key = lambda x: (x[1],x[0]))      # 뒷 타임 기준으로 정렬

    end = 0
    cnt = 0
    for st,en in schedule:                  # 시작, 끝 언패킹 후 순회
        if st >= end :                      # 시작이 전타임의 끝과 비교해서 더 크거나 같으면
            end = en                        # end를 다시 설정하고
            cnt += 1                        # cnt + 1
    print(f"#{idx+1} {cnt}")                
'''

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


