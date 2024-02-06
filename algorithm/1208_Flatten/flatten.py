'''
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 

최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
'''
import sys
sys.stdin = open("input.txt")
T = 10
for test_case in range(1,T+1):

    N = int(input())
    a = [0]*101
    n_list = list(map(int,input().split()))
    max_n = 0
    min_n = 0
    for n in n_list: # 카운팅정렬. 해당 층 수 카운트 +=1
        a[n] += 1
    for i in range(100,-1,-1):#위에서부터
        if i == 0: #0은 빼
            pass
        while a[i] != 0 and N != 0: #횟수 남았고 0 아니면
            a[i] -= 1
            a[i-1] += 1
            N -= 1 #위에놈 이동,횟수 마이너스
            for j in range(101):
                if a[j] != 0:
                   a[j] -= 1
                   a[j+1] += 1 #최소값 이동,횟수 마이너스, 브랰
                   break
        if N == 0 and a[i] != 0:
            max_n = i #다 끝났을때의 i 값( 최대값
            break
        elif a[i] == 0:
            max_n = i-1

    for j in range(101): #최소값 구하기
        if a[j] != 0:
            min_n = j
            break
    print(f'#{test_case} {max_n - min_n}')
    
'''
import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    h_cnt = [0] * 101   # 높이 카운트 -> 100이라는 높이를 이용할 것이므로 101
    min_v = 101         # 최소, 최대 비교 대상 초기화
    max_v = 0

    # 박스의 높이를 카운트 하면서(h_cnt) 최고점과 최저점을 찾기
    for i in range(100):
        h_cnt[boxes[i]] += 1    # box의 높이가 1 -> 높이가 1인 박스의 수 1 증가

        # 최대, 최소 값 갱신
        if boxes[i] > max_v:
            max_v = boxes[i]
        if boxes[i] < min_v:
            min_v = boxes[i]

    # 덤프 횟수가 다했거나
    # 덤프 횟수는 남았지만 (최대 - 최소) 크기 차이가 1 이상인경우 여기서 차이
    while dump > 0 and max_v - min_v > 1:
        # 평탄화를 한다 == 제일 높은 곳에서 제일 낮은 곳으로 박스를 하나 옮긴다.
        # 박스 높이가 1이었던 박스가 하나 적어진다
        # 박스 높이가 100이었던 박스가 하나 적어진다.
        h_cnt[min_v] -= 1
        h_cnt[max_v] -= 1

        # 박스 높이가 99인 박스가 하나 증가한다
        # 박스 높이가 2인 박스가 하나 증가한다
        h_cnt[min_v+1] += 1
        h_cnt[max_v-1] += 1

        # 지금 조사중인 제일 작은 박스가 더 이상 안남았다면
        # 다음 작은 박스로 조사 대사 이동
        if h_cnt[min_v] == 0:
            min_v += 1

        # 위와 동일
        if h_cnt[max_v] == 0:
            max_v -= 1

        # 한 번 덤프
        dump -= 1
    result = max_v - min_v
    print(f'#{tc} {result}')
'''
'''
import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    dump = int(input())
    matrix = list(map(int, input().split()))

    matrix.sort()   # 정렬 한다
    while dump:         # 덤프 가능한 동안 반복
        matrix[0] += 1
        matrix[-1] -= 1
        matrix.sort()
        dump -= 1

    print(f'#{tc} {matrix[-1] - matrix[0]}')
''' #개사기

'''
import sys #sort() 대신 버블솔트 사용한다는 점만 빼면 위와 동일
sys.stdin = open('input.txt')

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for tc in range(1, 11):
    dump = int(input())
    matrix = list(map(int, input().split()))

    bubble_sort(matrix) # 정렬 한다
    while dump:         # 덤프 가능한 동안 반복
        matrix[0] += 1
        matrix[-1] -= 1
        bubble_sort(matrix)
        dump -= 1

    print(f'#{tc} {matrix[-1] - matrix[0]}')
'''

'''
import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):

    dump = int(input())
    height = list(map(int, input().split()))

    while dump > 0: # 덤핑이 0보다 큰 동안. sort하지않고 max와 index로.
        max_height = height.index(max(height)) # 추가
        min_height = height.index(min(height)) # 추가

        height[max_height] -= 1 # 가장 큰 높이에서 1씩 빼기
        height[min_height] += 1 # 가장 낮은 높이에서 1씩 추가
        dump -= 1 # 덤프를 하나씩 차감

    if max(height) - min(height) <= 1: # 만약 덤프가 남았는데 가장 큰 높이와 낮은 높이의 차가 1이하라면
        break # 종료

    result = max(height) - min(height) # 최종 큰 높이 - 낮은 높이 산출
    print(f'#{test_case} {result}')'''