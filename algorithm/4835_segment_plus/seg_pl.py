'''

N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
 

다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.

이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
 
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12

답은 12와 6의 차인 6을 출력한다.


'''
import sys
sys.stdin = open("input.txt")
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))

    temp = []

    for i in range(len(n_list) - M + 1):
        sum_n = 0
        for m in range(M):
            sum_n += n_list[i + m]#슬라이싱으로 해도 됐을 듯. 슬라이싱은 유두리가 있으니까
        temp.append(sum_n)

    print(f'#{test_case} {max(temp) - min(temp)}')

'''
#나는 리스트에 다 넣고 최소값, 최대값 출력. 밑에는 하나하나 비교
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    # 최댓값 비교 대상 가장 작은 경우의 수 0
    max_num = 0
    # 최솟값 비교 대상 가장 큰 경우의 수
    # a가 가질 수 있는 최대 크기 10000
    # 구간합의 범위 M
    min_num = 10001 * M
    # N개의 정수, M개의 범위
    # 10 - 3 => 7 | 7개의 정수를 대상으로 조사
    for i in range(N - M + 1):
        temp = 0
        # 내 현재 위치부터 M개 까지
        for j in range(i, i + M):
            temp += ai[j]
        if max_num < temp:
            max_num = temp
        if min_num > temp:
            min_num = temp
    result = max_num - min_num
    print(f'#{tc} {result}')

'''