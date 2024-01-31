'''
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
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
    for n in n_list: # 카운팅정렬
        a[n] += 1
    for i in range(100,-1,-1):
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


