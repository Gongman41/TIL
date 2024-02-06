'''
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.

이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
 
아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.


가로 길이는 항상 1000이하로 주어진다.

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)

각 빌딩의 높이는 최대 255이다.


#부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 조망권이 확보된 세대의 수를 출력한다.


총 10개의 테스트케이스가 주어진다.

각 테스트케이스의 첫 번째 줄에는 건물의 개수 N이 주어진다. (4 ≤ N ≤ 1000)

그 다음 줄에는 N개의 건물의 높이가 주어진다. (0 ≤ 각 건물의 높이 ≤ 255)

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다. (예시에서 빨간색 땅 부분)
 
'''

import sys 
sys.stdin = open('input.txt')
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    n_list = list(map(int, input().split()))
    count = 0
    for n in range(2, len(n_list) - 2):
        if (n_list[n] - max([n_list[n - 2], n_list[n - 1], n_list[n + 1], n_list[n + 2]])) >= 0:
            count += (n_list[n] - max([n_list[n - 2], n_list[n - 1], n_list[n + 1], n_list[n + 2]]))
#슬라이싱한다음 n_list[n]이 max값일 때 n_list[n]을 빼고 나머지의 max값을 빼는 것도 낫뱃 
    print(f'#{test_case} {count}') #완탐

'''
import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    data = list(map(int, input().split()))
    
    result = 0
    min_value = 256
    for i in range(2, N -2):
        for j in range(5):
            if j != 2:
             if data[i] - data[i-2+j] < min_value:
                min_value = data[i] - data[i-2+j]
        if min_value > 0:
            result += min_value
    print(result)  # 나랑 차이는 빼는 애들에 max를 썼냐 아니면 빼고 난 다음 값에 min을 썼냐      
    
'''

'''
for i in range(2,N-2):
    max_neighbor = 0
    for j in range(i-2,i+3):
        if i == j: continue
        if data[j] > data[i] and max_neighbor < data[j]:
            max_neighbor = data[j] 
        elif data[j] >= data[i]:
            max_neighnor = data[i]
            break
    result += data[i] - max_neighbor #이웃중에 최대값 찾기. 조사중에 취소됐으면 += 0
print(result)
'''

