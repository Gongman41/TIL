import sys
sys.stdin = open('input.txt')

def check_right(srt,m):
    sct_num = ''
    global full_sct_num
    full_sct_num = []
    for i in range(8):
        if srt+7*(i+1) >= m:
            return 0
        sct_num = ''.join(secret[srt+7*i:srt+7*(i+1)]) #zip인가 뭐로

        if sct_num == '0001101':
            full_sct_num.append(0)
        elif sct_num == '0011001':
            full_sct_num.append(1)
        elif sct_num == '0010011':
            full_sct_num.append(2)
        elif sct_num == '0111101':
            full_sct_num.append(3)
        elif sct_num == '0100011':
            full_sct_num.append(4)
        elif sct_num == '0110001':
            full_sct_num.append(5)
        elif sct_num == '0101111':
            full_sct_num.append(6)
        elif sct_num == '0111011':
            full_sct_num.append(7)
        elif sct_num == '0110111':
            full_sct_num.append(8)
        elif sct_num == '0001011':
            full_sct_num.append(9)
        else:
            return 0 
    return 1


    
    
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    secret = []
    one_point = 0
    full_sct_num = []
    for n in range(N):
        tem = input()
        if '1' in tem:
            secret = tem

            #3:2,3:1,2:2,2:1,1:4,1:1,1:2,1:1,1:3.1:2
    one_point = secret.index('1')
    if 0 <= one_point-3:
        for pnt in range(one_point-3,one_point):
            if  check_right(pnt,M):

                break
    elif 0 <= one_point-2:
        for pnt in range(one_point-2,one_point):  
            if  check_right(pnt,M):
                break 
    elif 0 <= one_point-1:
        for pnt in range(one_point-1,one_point):
            if  check_right(pnt,M):
                break
    if not full_sct_num:
        print(f'#{tc} 0')
    else:
        result = 0
        for f in range(4):
            result += full_sct_num[2*f]*3 + full_sct_num[2*f+1]
        if result % 10 == 0:
            print(f'#{tc} {sum(full_sct_num)}')
        else:
            print(f'#{tc} 0')


                

    

