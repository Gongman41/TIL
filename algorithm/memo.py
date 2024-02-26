T = int(input())
for tc in range(1,T+1):
    D,A,B,F = map(int,input().split())
    f_m = D/(B+F)
    s_m = D/(A+B) - f_m
    print(f'#{tc} {f_m*F + s_m*B}')

                    
                    
                    
                    
                
        
    
        