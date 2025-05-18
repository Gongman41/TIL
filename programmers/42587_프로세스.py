from collections import deque
def solution(priorities, location):
    q = []
    for i in range(len(priorities)):
        if i == location:
            q.append([priorities[i],True])
        else:
            q.append([priorities[i],False])
    q = deque(q)
    cnt = 0
    while q:
        cur_lst = q.popleft()
        for qq in q:
            if qq[0] > cur_lst[0]:
                q.append(cur_lst)
                break
        else:
            cnt += 1
            if cur_lst[1] == True:
                return cnt
    