import sys
sys.stdin = open("sample_input.txt")
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    n_st_list = []
    for n in range(N):
        n_st_list.append(input())
    end_point =False
    line_n_st_list = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(n_st_list[j][i])

        line_n_st_list.append(temp)
    for n in range(N):
        for nm in range(N-M+1):
            if n_st_list[n][nm:nm+M] == n_st_list[n][nm:nm+M][::-1]:
                print(f"#{tc} {str(n_st_list[n][nm:nm+M])}")
                end_point = True
                break
            if line_n_st_list[n][nm:nm+M] ==line_n_st_list[n][nm:nm+M][::-1]:
                print(f"#{tc} {''.join(line_n_st_list[n][nm:nm+M])}")
                end_point = True
                break
        if end_point == True:
            break


