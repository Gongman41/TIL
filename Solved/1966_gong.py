from collections import deque
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    deq = deque(list(map(int,input().split())))
    count_lst = [0]*11
    cnt = 0
    for n in deq:
        count_lst[n] += 1

    while deq:

        if M == 0:
            a = deq.popleft()
            if count_lst[a+1:] == [0] * (10-a):
                count_lst[a] -= 1
                cnt += 1
                break
            else:
                deq.append(a)
            M += len(deq)-1




        else:
            a = deq.popleft()
            if count_lst[a+1:] == [0] * (10-a):
                count_lst[a] -= 1
                cnt += 1
            else:
                deq.append(a)

            M -= 1
    print(cnt)