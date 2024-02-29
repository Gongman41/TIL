T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    boong_time = [0] * 11112
    roop = 1
    for i in range(11112):
        if roop*M <= i <(roop+1)*M:
            boong_time[i] = K*roop
        if i == M*(roop+1)-1:
            roop += 1
    boong_stack_mns = 0
    last_time = 0
    check = True
    time_lst = list(map(int,input().split()))
    time_lst.sort()
    for time in time_lst:

        if boong_time[time] - boong_stack_mns >= 1:
            boong_stack_mns += 1
        else:
            check = False
            print(f'#{tc} Impossible')
            break
    if check == True:
        print(f'#{tc} Possible')



