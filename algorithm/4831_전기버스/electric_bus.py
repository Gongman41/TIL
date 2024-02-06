'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
 
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    K,N,M = map(int,input().split())
    st_point_list = list(map(int,input().split()))
    current = 0
    count = 0
    temp_max = 0
    while True:
        arr = False
        for k in range(K):

            current += 1
            if current == N:
                break

            for st_po in st_point_list:
                if current == st_po:
                    temp_max = current
                    arr = True
        if current == N:
            break

        if arr == False:
            count = 0
            break
        else:
            current = temp_max
            count += 1

    print(f'#{tc} {count}')
#현재 위치에서 K거리 안에있는 정류소 중 제일 먼 곳으로 현재 위치 갱신
#반복
    
'''
import sys
sys.stdin = open('input.txt')


# gas : 이동 가능 횟수
# now : 현재 정류장 위치
# cnt : 충전 횟수

def go(gas, now, cnt):
    global result
    # 지금까지 충전한 횟수가
    # 언젠가 누군가 종착점에 도착할때까지 들었던 충전 횟수보다 크다면
    # 더 이상 조사할 의유 없음
    if cnt > result:
        return
    # 종착점 도착하면 멈춤
    if now == N:
        # 지금까지 충전한 횟수를 result에 넣을거에요.
        result = cnt
        return
    if station[now]:
        # 충전 했으니 이동 가능 횟수 K
        # 충전하고 다음칸으로 갈때 가스 1 든다
        go(K-1, now+1, cnt+1)
    if gas:
        # 현재 위치에 충전소가 없으면 그냥 한칸 이동
        # 가스가 남아 있다면
        go(gas-1, now+1, cnt)


T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # 실제 모든 정류장
    station = [0] * (N+1)
    # 정류장에 충전소 위치 표기
    for index in range(M):
        station[data[index]] = True
    # 최종 결괏값 : 최소 충전 횟수가 조건
    # 최악의 경우를 상정
    result = N+1
    # 출발시 최대치 가스 가지고 시작 : K
    # 시작 위치 0
    # 충전 횟수 0
    go(K, 0, 0)
    # 모든 경우의수 다 확인했는데 result가 그대로다? 도착못했다
    if result == N+1:
        result = 0
    print(result)'''
#그냥 잘 풀어 쓴거 같은데. 정류장을 리스트에 따로 표기한 정도

'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))

    loc = 0 # 현재 위치
    count = 0 # 충전 횟수

    while loc + K < N:
    # 현재 위치 + 최대 이동거리가 종점에 도착하지 않을 동안 반복
        for step in range(K, 0, -1):
        # 최대한 멀리있는 정류장에서 충전하는 것이 최소 충전 횟수
            if loc + step in stations:
                loc += step
                count += 1
                break
        else:
        # 종점에 도착8할 수 없는 경우 = step이 0이 되었는데 충전소가 나타나지 않은 경우
            count = 0
            break

    print(f'#{test_case} {count}')
    ''' #K를 거꾸로 세는 건 좋네. 제일 먼 값, max값.for else 문


