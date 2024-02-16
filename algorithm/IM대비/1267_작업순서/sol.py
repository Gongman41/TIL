import sys
sys.stdin = open('input.txt')
T = 10
for tc in range(1,T+1):
    V,E = map(int,input().split())
    lst = list(map(int,input().split()))
    V_list = list(range(V))
    start_list = list(range(1,V+1))
    line_dict = {}
    for i in range(E):
        if start_list.find(lst[2 * i + 1]) != -1:
            start_list.pop(start_list.find(lst[2*i+1]))
        if line_dict.setdefault(lst[2*i],[lst[2*i+1]]) != [lst[2*i+1]]:
            line_dict[lst[2*i]].append(lst[2*i+1])



