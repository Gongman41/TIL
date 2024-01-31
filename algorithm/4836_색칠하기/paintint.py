'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    matrix = [[0]*10 for _ in range(10)]
    N = int(input())
    p_count = 0 #보라색 카운트
    for n in range(N):
        c1,r1,c2,r2,color = map(int,input().split()) #현재 입력된 범위, 색 저장
        for _c in range(c1,c2+1):
            for Ic in range(r1,r2+1):
                if matrix[_c][Ic] == 0: #색칠 안했으면 색칠
                    matrix[_c][Ic] = color
                elif matrix[_c][Ic] != color: #색칠이 이미 됐는데 같은 색 아님.
                    p_count +=1 # 카운트만 하기. 같은 색이면 지나감.
    print(f'#{tc} {p_count}')




