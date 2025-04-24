import sys
from collections import deque

input = sys.stdin.readline

def DSLR(num, command):
    if command == 'D':
        return (2 * num) % 10000
    elif command == 'S':
        return 9999 if num == 0 else num - 1
    elif command == 'L':
        return (num % 1000) * 10 + num // 1000  # 왼쪽 회전
    else:  # 'R'
        return (num % 10) * 1000 + num // 10  # 오른쪽 회전

T = int(input())
for _ in range(T):
    st, tr = map(int, input().split())
    visited = [False] * 10000  # 방문 여부 체크
    q = deque([(st, '')])  # (현재 숫자, 명령어 문자열)
    visited[st] = True

    while q:
        cur, command = q.popleft()

        if cur == tr:
            print(command)
            break  # 정답을 찾으면 종료

        for c in 'DSLR':
            tem = DSLR(cur, c)  # 현재 숫자에서 DSLR 변환 수행
            if not visited[tem]:
                visited[tem] = True
                q.append((tem, command + c))
