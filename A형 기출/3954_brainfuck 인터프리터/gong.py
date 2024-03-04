# import sys
# sys.stdin = open("input.txt")
t = int(input())
for tc in range(t):
    sm,sc,si = map(int,input().split())
    sm_lst = [0]*sm
    sc_lst = input()
    si_lst = input()
    cov_lst = []
    r_cov_lst = []
    sm_i = 0
    sc_i = 0
    si_i = 0
    fin = False
    cnt = 0
    while sc_i != sc:
        if sc_lst[sc_i] == '+':
            check = 0
            while type(sm_lst[sm_i]) == str:
                sm_i = (sm_i + 1)%sm
                check += 1
                if check >= sm:
                    
                    break # 전체 뿐만 아니라 루프 공간 안에서도
                
            else: #내가 생각한 느낌의 반대
                sm_lst[sm_i] += 1
                
            if check > sm:
                    
                break # 전체 뿐만 아니라 루프 공간 안에서도
                
            
            
        elif sc_lst[sc_i] == '-':
            check = 0
            while type(sm_lst[sm_i]) == str:
                sm_i = (sm_i + 1)%sm
                check += 1
                if check > sm:
                    
                    break
                
            else: #내가 생각한 느낌의 반대
                sm_lst[sm_i] -= 1
        
            if check > sm:
                    
                break # 전체 뿐만 아니라 루프 공간 안에서도
             
        elif sc_lst[sc_i] == '<':
            sm_i = (sm + sm_i - 1)%sm
        elif sc_lst[sc_i] == '>':
            sm_i = (sm_i+1)%sm
        elif sc_lst[sc_i] == ',':
            if si-1 > si_i:
                sm_lst[sm_i] = si_lst[si_i]
                sm_i += 1
                si_i += 1
            elif si-1 == si_i:
                sm_lst[sm_i] = 255
            else:
                fin = True
                break
        elif sc_lst[sc_i] == '[':
            if sm_lst[sm_i] == 0:
                while sc_lst[sc_i] != ']':
                    sc_i += 1
            else:
                cov_lst.append(sc_i)
        elif sc_lst[sc_i] == ']':
            if sm_lst[sm_i] != 0:
                if r_cov_lst == [] or r_cov_lst[-1] != sc_i:
                    r_cov_lst.append(sc_i)
                sc_i = cov_lst[-1]
            else:
                cov_lst.pop()
                if r_cov_lst[-1] == sc_i:
                    r_cov_lst.pop()         
        sc_i += 1
        cnt += 1
        if cnt >= 50000000:
            break
        
    
    
    
    if sc_i == sc or fin == True:
        print('Terminates')
    else:
        print('Loops',cov_lst[-1],r_cov_lst[-1])
    print(sm_lst)

