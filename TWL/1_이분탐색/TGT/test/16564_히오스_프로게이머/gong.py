import sys
N,K = map(int,sys.stdin.readline().split())
# 팀 목표레벨을 이진으로. 총합을 초과하면 밑으로.
n_lst = []
start = 0

for _ in range(N):
    n_lst.append(int(sys.stdin.readline()))
    start = min(start,n_lst[-1])
end = start + K
n_lst.sort()
def check_sum(lst,lv,k):
    start = 0
    end = len(lst)-1
    
    while start <= end:
        middle = (start+end)//2
        if lst[middle] > lv:
            end = middle -1
        elif lst[middle] == lv:
            index = middle
            break
        else:
            start = middle +1
    else:
        index = end
    print(index)
    for i in range(index+1):
        k -= lst[i]
        if k <0:
            return False
    return True

while start <= end:
    level = (start+end)//2
    #레벨은 이진으로, 근데 총합이 넘는지 안넘는지는?
    # n_lst를 정렬해서 목표레벨보다 낮은 값을 이진으로 찾은다음
    #거기서부터 계산_최악일경우 더 최악, 
    if check_sum(n_lst,level,K):
        start = level +1
    else:
        end = level -1
print(level)
    
    

    
    