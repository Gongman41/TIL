'''
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 
수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''
N,S = map(int,input().split())
n_lst = list(map(int,input().split()))
cnt = 0
for n in range(1<<N):
    sum_n = []
    
    for i in range(N):
        if n & (1<<i):
            sum_n.append(n_lst[i])
    
    if sum_n !=[] and sum(sum_n) == S:
        cnt+=1
print(cnt)
        