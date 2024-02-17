import sys
sys.stdin = open('input.txt')
T = 10

def gogo(srt):
    if line_dict.get(srt) != None :
        for i in line_dict[srt]:
            if serveral_count[i] == 1:
                stack.append(i)
                result.append(i)
                serveral_count[i] -= 1
                gogo(i)
            elif serveral_count[i] > 1:
                serveral_count[i] -= 1
    if stack:
        gogo(stack.pop())

        
for tc in range(1,T+1):
    V,E = map(int,input().split())
    lst = list(map(int,input().split()))
    line_dict = {}
    serveral_count = [0]*(V+1)#목적지 언급 수
    start_list = []
    stack = []
    result = []
    for i in range(E):
        serveral_count[lst[2 * i + 1]]+=1
        if line_dict.setdefault(lst[2*i],[lst[2*i+1]]) != [lst[2*i+1]]:#키에 값이 안들어 가 있으면 여기서 넣고 있으면 다른 값이 반환돼서 append
            line_dict[lst[2*i]].append(lst[2*i+1])
    for i in range(1,len(serveral_count)):
        if serveral_count[i] == 0:
            start_list.append(i)
    for start in start_list:
        result.append(start)
        gogo(start)
    print(f'#{tc} ',end = '')
    print(*result)
        
    
        
            



