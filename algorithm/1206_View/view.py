T = 10
for test_case in range(1, T + 1):
    N = int(input())
    n_list = list(map(int, input().split()))
    count = 0
    for n in range(2, len(n_list) - 2):
        if (n_list[n] - max([n_list[n - 2], n_list[n - 1], n_list[n + 1], n_list[n + 2]])) >= 0:
            count += (n_list[n] - max([n_list[n - 2], n_list[n - 1], n_list[n + 1], n_list[n + 2]]))

    print(f'#{test_case} {count}')

'''
import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    data = list(map(int, input().split()))
    
    result = 0
    
    for i in range(2, N -2):
        for j in range(5):
            if j != 2:
             if data[i] - data[i-2+j] < min_value:
                min_value = data[i] - data[i-2+j]
        if min_value > 0:
            result += min_value
    print(result)        
'''

'''
for i in range(2,N-2):
    max_neighbor = 0
    for j in range(i-2,i+3):
        if i == j: continue
        if data[j] > data[i] and max_neighbor < data[i]:
            max_neighbor = data[j]
        elif data[j] >= data[i]:
            break
    result += data[i] - max_neighbor
'''

