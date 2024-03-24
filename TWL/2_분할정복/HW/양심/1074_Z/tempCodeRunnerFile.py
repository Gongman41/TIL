def where_a_y(n,cnt,r,c):
    if n == 1:
        if r == 0 and c == 0:
            print(cnt+1)
            return
        elif r == 0 and c == 1:
            print(cnt+2)
            return
        elif r == 1 and c == 1:
            print(cnt+3)
            return
        else:
            print(cnt+4)
            return
    if r < 2**(n-1) and c < 2**(n-1):
        where_a_y(n-1,cnt,r,c)
    elif r >= 2**(n-1) and c< 2**(n-1):
        where_a_y(n-1,cnt+2**(2*n-1),r-2**(n-1),c)
    elif r>= 2**(n-1) and c >= 2**(n-1):
        where_a_y(n-1,cnt+2**(2*n-2)*3,r-2**(n-1),c-2**(n-1))
    else:
        where_a_y(n-1,cnt+2**(2*n-2),r,c-2**(n-1))
    
N,r,c = map(int,input().split())
# 큰 것보다 부분으로 쪼개기
if N == 1:
    if r == 0 and c == 0:
        print(0)
            
    elif r == 0 and c == 1:
        print(1)
    
    elif r == 1 and c == 1:
        print(2)
        
    else:
        print(3)
else:     
    where_a_y(N,0,r,c)
