'''
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.
'''
import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):
    t = int(input())
    _sum_list = [0]*100
    Isum_list = [0]*100
    l_r_sum = 0
    r_l_sum = 0 #가로,세로,왼_오 대각선, 오_왼 대각선
    for n in range(100):
        temp = list(map(int,input().split())) #임시리스트에 행 100번받기
        for m in range(100):# 열
            _sum_list[n] += temp[m] #가로는 해당 행에 열 값 다 더하기
            Isum_list[m] += temp[m] #세로는 해당 열에 행 값 더하기
            if n == m:
                l_r_sum += temp[m] #대각선은 대각선에 있는 값만 더하기
            if n == 99 - m:
                r_l_sum += temp[m]
    max_n = max(max(Isum_list), max(_sum_list),l_r_sum, r_l_sum) #최강자전
    print(f'#{t} {max_n}')
