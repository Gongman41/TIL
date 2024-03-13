N,M = map(int,input().split())
#처음 구간의 값과 다음 구간의 값이 같은 경우. 그 값들 중 가장 작은 값
n_lst = list(map(int,input().split()))

# 최소를 구하는것. 초반 구간을 구하는 것
for i in range(N):
    sum_b = sum(n_lst[:i])
    start = 1
    end = i
    
    #M은 어떡해. 약간 러시아 국기.
    while start <= end:
        middle = (start+end)//2
        tem_sum = 0
        tem_md = middle
        cnt = 0
        while tem_sum < sum_b:
            tem_sum += n_lst[middle]
            tem_md += 1
        if tem_sum == sum_b:
            start,end = middle,tem_md
            cnt+=1
            if cnt == M:
                print(sum_b)
                break
            elif cnt > M:
                break
                
        elif cnt > M:
            break
                
        else:
            break
#초반 구간으로 블루레이 크기 구하고 그거가 되는 구간을 이진으로 갈기기

            
    