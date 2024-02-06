'''
0-9사이의 숫자 카드에서 임의의 카드 6장을 뽑는다. 3장의 카드가 연속적인 번호를 갖는 경우를  run,
3장의 카드가 동일한 번호를 갖는 경우를 triplet. 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다
숫자를 입력받아 baby-gin여부를 판단하는 프로그램을 작성하여라.

트리플렛 2세트
런 2세트
트리플렛 1세트 런 1세트
    런1세트안에 트리플렛 1세트 한장은 랜덤.
    런 바깥에 트리플렛 1세트
'''


import sys
sys.stdin = open('input.txt')


def check(n):
    flag = 0                    # triplet or run이 몇번 나왔는지 체크
    while True:                 # 아래 조건을 만족할때까지 반복
        if visited[n] >= 3:     # n번이 3번 이상 나왔다면 triplet 먼저 체크
            flag += 1           # 횟수 증가
            visited[n] -= 3     # 한번 체크 했으므로 해당 수 제거
        # n이 7이하일때만 run 검증 (index를 넘지 않도록)
        elif n <= 7 and visited[n] >= 1 and visited[n + 1] >= 1 and visited[n + 2] >= 1:
            flag += 1
            visited[n] -= 1     # n번 부터 연달아 있는 3개의 수 체크
            visited[n + 1] -= 1
            visited[n + 2] -= 1
        else:                   # 위 조건을 모두 만족하지 못하는경우 발생시
            return flag         # 지금까지 기록한 triplet, run의 개수를 반환하고 종료


T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input()))

    visited = [0] * 10          # 0-9번 수가 몇번 나왔는지 체크하기 위한 리스트
    for i in range(6):
        visited[numbers[i]] += 1

    result = 0
    for n in range(10):         # 모든 수에 대해서 triplet or run 검증
        result += check(n)      # 반환된 값 누적

    print(f'#{tc}', end=' ')    # 누적된 결과에 따라 정답 출력
    print(1) if result >= 2 else print(0)


'''
    import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    data = list(map(int, input().strip()))
    cards = [0] * (max(data)+1)  # 카드 count 배열 초기화

    # 카드 갯수 카운트
    for i in data:   
        cards[i] += 1

    idx = cnt = 0  # 반복문 제어 idx / 정답 카운트 변수 cnt

    # 같은 값이 3개 이상 있을 때
    while idx < len(cards):
        if cards[idx] >= 3:
            cards[idx] -= 3
            cnt += 1  # baby gin 카운트 증가
            continue  # 5555555 와 같은 경우를 위해 continue
        idx += 1

    idx = 1  # run의 경우 검사를 위한 idx 초기화
    while idx < len(cards)-1:  # 끝까지 검사할 경우 인덱스 에러 발생
        if cards[idx - 1] >= 1 and cards[idx + 1] >= 1 and cards[idx] >= 1:
            cards[idx-1] -= 1
            cards[idx] -= 1
            cards[idx+1] -= 1
            cnt += 1
            continue  # 123123 와 같은 경우를 위해 continue
        idx += 1

    print(f'#{tc} 1') if cnt == 2 else print(f'#{tc} 0')
'''
#비슷한데