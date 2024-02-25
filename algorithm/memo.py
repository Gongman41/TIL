T = int(input())
for tc in range(1,T+1):
    N = int(input())
    n_list = [list(map(int,input().split())) for _ in range(N)]
    min_n = 10e10
    for n in range(N):
        no_lst = [n]
        tem = n_list[0][n] 
        for i in range(1,N):
            tem_min = 10e10
            no_n = 0
            for j in range(N):
                if j not in no_lst and n_list[i][j] <tem_min:
                    tem_min = n_list[i][j]
                    no_n = j
            tem += tem_min
            no_lst.append(no_n)
        min_n = min(min_n,tem)
    print(f'#{tc} {min_n}')
                    
                    
                    
                    
                
        
    
        