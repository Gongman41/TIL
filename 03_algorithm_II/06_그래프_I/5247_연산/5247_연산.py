import sys
from collections import deque
sys.stdin = open('input.txt')
#계산하고 값 리턴하는 함수
def cont(cur,cnt,target,number):
    global min_n
    if cur < 0 or cur > 1000000:
        return -100,-100
    # 범위 벗어나는 애들 continue
    if cur == target:
        min_n = min(min_n,cnt)
        return 'STOP','STOP'
    # 최소값 나오면 break

    if number == 0:
        return cur + 1, cnt + 1
    elif number == 1:
        return cur*2, cnt +1
    elif number == 2:
        return cur-1, cnt +1
    else:
        return cur - 10, cnt + 1



T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    min_n = 10e10
    cont_deq = deque([[N,0]])
    tem = []
    visited = [0]*2000001
    while cont_deq:
        cur, cnt = cont_deq.popleft()

        for i in range(4):
            tem = cont(cur,cnt,M,i)


            if tem[0] =='STOP':
                break
            if tem[0] < 0 or visited[tem[0]] == 1 :
                continue
            visited[tem[0]] = 1
            cont_deq.append(tem)
        # deque에서 빼낸 값 visited처리하고 append. 최소값 찾으면 break,
        if tem[0] == 'STOP':
            break
    print(f'#{tc} {min_n}')
