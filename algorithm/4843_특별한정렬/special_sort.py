'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5
 

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
'''

import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
   N = int(input())
   n_list = list(map(int,input().split()))
   n_list.sort()
   nn = 0
   while nn != N:
       if nn == 0 or nn%2 == 0:
           n_list.insert(nn,n_list.pop())
       nn+= 1


   print(f'#{tc}',end = " ")
   for n in range(10):
       if n == 9:
           print(f'{n_list[n]}')
           break
       print(f'{n_list[n]}',end = " ")


'''
def bubble_sort():
    for i in range(N-1, 0, -1):
        for j in range(i):
            if i % 2:
                if ai[j] > ai[j + 1]:
                    ai[j], ai[j + 1] = ai[j + 1], ai[j]
            else:
                if ai[j] < ai[j + 1]:
                    ai[j], ai[j + 1] = ai[j + 1], ai[j]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    bubble_sort()
    ai.reverse()
    print(f'#{tc}', *ai[:10])
'''# sort 대신 bubble sort로 정렬

'''
import sys
sys.stdin = open('input.txt')

def counting_sort():
    counting_arr = [0] * 101
    sorted_ai = [0] * N
    for num in ai:
        counting_arr[num] += 1

    for index in range(1, 101):
        counting_arr[index] += counting_arr[index - 1]

    for index in range(N):
        sorted_ai[counting_arr[ai[index]]-1] = ai[index]
#여까지 정렬
    for i in range(N//2):
        result[i*2] = sorted_ai[len(sorted_ai) - 1 - i]
        result[i*2+1] = sorted_ai[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    result = [0] * N
    counting_sort()

    print(f'#{tc}', *result[:10])
'''

'''
import sys
sys.stdin = open('input.txt')

def selection_sort():
    for x in range(10):
        mIdx = x
        for y in range(x + 1, N):
            if x % 2:
                if ai[mIdx] > ai[y]:
                    mIdx = y
            else:
                if ai[mIdx] < ai[y]:
                    mIdx = y
        ai[x], ai[mIdx] = ai[mIdx], ai[x]
#앞에 상태변경을 x%2로 바꾼느낌
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    selection_sort()
    # result = ' '.join(map(str, ai[:10]))
    print(f'#{tc}', *ai[:10])


'''

'''
import sys
sys.stdin = open('input.txt')

def min_max():
    DESC_ASC = 'DESC'   # 첫 정렬 -> DESC
    for i in range(N):
        max_value = ai[i]
        max_idx = i
        min_value = ai[i]
        min_idx = i
        for j in range(i + 1, N): # 내 다음 위치랑 나랑 비교
            if max_value < ai[j]:
                max_value = ai[j]
                max_idx = j
            if min_value > ai[j]:
                min_value = ai[j]
                min_idx = j
        if DESC_ASC == 'DESC':
            ai[i], ai[max_idx] = ai[max_idx], ai[i]
            DESC_ASC = 'ASC'
        else:
            ai[i], ai[min_idx] = ai[min_idx], ai[i]
            DESC_ASC = 'DESC' #처리하고 상태변경 버블소트 느낌



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    min_max()
    print(ai)
'''