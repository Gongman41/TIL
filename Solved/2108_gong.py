N = int(input())
plus_n = [0]*4001
minu_n = [0]*4000
min_n = 10e10
max_n = -10e10
middle = N//2+1
max_cnt = [-4001,-4001]
cnt = 0
m = 0
for _ in range(N):
    a = int(input())
    if a >= 0 :
        plus_n[a] += 1
        if plus_n[a] > cnt:
            cnt = plus_n[a]
            max_cnt = [a,a]
        elif plus_n[a] == cnt:
            if max_cnt[1] > a:
                max_cnt[0],max_cnt[1] = max_cnt[1],a
            elif max_cnt[0] > a >= max_cnt[1]:
                max_cnt[0] = a
            elif max_cnt[0] < a and max_cnt[1] == max_cnt[0]:
                max_cnt[0] = a

    else:
        minu_n[-a] += 1
        if minu_n[-a] > cnt:
            cnt = minu_n[-a]
            max_cnt = [a,a]
        elif minu_n[-a] == cnt:
            if max_cnt[1] > a:
                max_cnt[0],max_cnt[1] = max_cnt[1],a
            elif max_cnt[0] > a >= max_cnt[1]:
                max_cnt[0] = a
            elif max_cnt[0] < a and max_cnt[1] == max_cnt[0]:
                max_cnt[0] = a

    min_n = min(min_n,a)
    max_n = max(max_n,a)
    m+= a
print(int(round((m/N),0)))
cnt = 0
for n in range(min_n,max_n+1):
    if n<0 and minu_n[-n]!=0:
        
        cnt+= minu_n[-n]
        if cnt >= middle:
            print(n)
            break
    elif n >=0 and plus_n[n] != 0:
        cnt += plus_n[n]
        if cnt >= middle:
            print(n)
            break
print(max_cnt[0])
print(max_n-min_n)
    #산술평균은 받으면서 더해서
    #최빈값은 제일 큰 cnt값이랑 같으면 더 작은 값을 저장
    #범위는 최댓값,최솟값받으면서 구하기
    #문제는 중앙값인데 이거는 중앙값을 계속 갱신하면서 해야될듯.근데 그러면 정렬해야되는데.





