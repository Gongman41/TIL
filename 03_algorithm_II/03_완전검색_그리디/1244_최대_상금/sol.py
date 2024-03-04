import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    n_list,cnt = input().split()
    cnt = int(cnt)
    n_list = list(map(int,n_list))
    sm_n_idx = []



    if cnt >= len(n_list)-1 :
        i = 0
        while cnt > 0 and i < len(n_list)-1:
            max_n = n_list[i]
            tem_i = -1
            for j in range(i+1,len(n_list)):
                if max_n <= n_list[j]:
                    tem_i = j
                    max_n = n_list[j]
            if tem_i != -1:
                n_list[i],n_list[tem_i] = n_list[tem_i],n_list[i]
                cnt -= 1
            else:
                i += 1

        for n in range(len(n_list) - 1):
            if n_list[n] == n_list[n + 1]:
                sm_n_idx = [n,n+1]
                break
        while cnt > 0:
            if sm_n_idx:
                n_list[sm_n_idx[0]],n_list[sm_n_idx[1]] = n_list[sm_n_idx[1]],n_list[sm_n_idx[0]]
                cnt -= 1
            else:
                n_list[-1], n_list[-2] = n_list[-2], n_list[-1]
                cnt -= 1
    else:
        i = 0

        while cnt > 0:
            # max_n = n_list[i]
            # tem_i = -1
            # for j in range(i+1,len(n_list)):
            #     if max_n <= n_list[j]:
            #         tem_i = j
            #         max_n = n_list[j]
            # if tem_i != -1:
            #     n_list[i],n_list[tem_i] = n_list[tem_i],n_list[i]
            #     cnt -= 1
            # i += 1

            max_n = n_list[i]
            tem_i = [0]
            power = 1

            for n in range(len(n_list) - 1):
                if n_list[n] == n_list[n + 1]:
                    sm_n_idx = [n, n + 1]
                    break

            for j in range(i + 1, len(n_list)):
                if max_n < n_list[j]:
                    tem_i = [j]
                    max_n = n_list[j]
                elif n_list[i] != n_list[j] and max_n == n_list[j]:
                    tem_i.append(j)
                elif n_list[i] > n_list[j]:
                    power += 1
            if tem_i == [0]:
                if n_list[i+1:] == sorted(n_list[i+1:],reverse=True):
                    if sm_n_idx:
                        n_list[sm_n_idx[0]], n_list[sm_n_idx[1]] = n_list[sm_n_idx[1]], n_list[sm_n_idx[0]]
                        cnt -= 1
                    else:
                        n_list[-1], n_list[-2] = n_list[-2], n_list[-1]
                        cnt -= 1
                else:
                    i+= 1
            elif len(tem_i) == 1:
                n_list[i], n_list[tem_i[0]] = n_list[tem_i[0]], n_list[i]
                cnt -= 1
                i += 1
            else:
                n_list[i], n_list[tem_i[-power]] =  n_list[tem_i[-power]], n_list[i]
                cnt -= 1
                i += 1




    print(f'#{tc}', ''.join([str(item) for item in n_list]))

'''
def backtrack(idx=0,result=0):                      # 대 트 래 킹
    if idx == cnt:
        ans.append(result)
        return
    
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            
            num[i], num[j] = num[j], num[i]

            result = int("".join(num))
            if (idx,result) not in visit:
                backtrack(idx+1,result) #본 배열의 요소의 위치 변경, result를 저장하는건 출력용
                visit.append((idx,result))

            num[i], num[j] = num[j], num[i]
            

for t in range(int(input())):
    num,cnt = input().split()
    num = list(num)
    cnt = int(cnt)
    visit = []
    ans = []

    backtrack()

    print(f"#{t+1} {max(ans)}")'''


