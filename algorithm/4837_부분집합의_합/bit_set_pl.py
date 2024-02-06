'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.


예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.


'''
import sys
sys.stdin = open('input.txt')

T = int(input())

def f(arr,N, K):
    arr_n = len(arr)
    set_count = 0
    for i in range(1<<arr_n): # 모든 부분집합 생성. 10진수가 아닌 2진수로 생각.1<<N 은 2^N을 의미. 등비수열의 합 ㅇㅇ
        s = 0
        count = 0
        for j in range(arr_n):# 모든 부분집합 각각의의 모든 원소 계산
            if i & (1<<j):#i의 j번 비트가 1인 경우 == 해당 원소가 현재 부분집합에 속하는지를 나타냄
                s += arr[j] #모든 부분집합 각각의 합계, 원소개수 저장
                count += 1
        if s == K and count == N:
            set_count+=1 #조건과 맞으면 +1
    return set_count

for tc in range(1,T+1):

    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    N,K = map(int,input().split())
    print(f"#{tc} {f(arr,N,K)}")

'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))

    for i in range(1 << 12):
        result = []
        for j in range(12):
            if i & (1 << j):
                result.append(arr[j])
        if len(result) == N and sum(result) == K:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')
'''
