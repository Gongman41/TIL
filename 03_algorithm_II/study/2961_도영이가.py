N = int(input())
sn_lst = [list(map(int,input().split())) for _ in range(N)]
# 재료를 쓰면 신맛은 곱해주고 쓴맛은 더해줌
min_n = 10e10
for i in range(1<<N):
    tem_lst = []
    tem_min = 10e10
    for n in range(N):
        if i &(1<<n):
            tem_lst.append(sn_lst[n])
    if tem_lst != []:
        if len(tem_lst) == 1:
            min_n = min(min_n,abs(tem_lst[0][0]-tem_lst[0][1]))
        else:
            s,b = tem_lst[0]
            for n in range(1,len(tem_lst)):
                s *= tem_lst[n][0]
                b += tem_lst[n][1]
            min_n = min(min_n,abs(s-b))
print(min_n)
            
            
            
        
            
            