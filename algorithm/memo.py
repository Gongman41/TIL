import sys
sys.stdin = open("sample_input.txt")
N = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
M = int(input())
m_list = list(map(int,input().split()))
count_list =[]

def ejinsearching(list,a):
    middle = len(list)//2
    if list[middle] == a:
        list.pop(middle)
        return True
    elif list[middle] > a:
        return ejinsearching(list[len(list)//2+1:],a)
    elif list[middle] < a:
        return ejinsearching(list[:len(list)//2], a)
for m in range(M):
    count = 0
    while ejinsearching(n_list,m_list[m]):
        count+=1
    count_list.append(count)
print(*count_list)























