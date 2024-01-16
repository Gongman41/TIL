T = int(input())
for t in range(T):
    N = int(input())
    number_list = []
    first_line = [0]*N
    second_line = [0]*N
    third_line = [0]*N
    print(f"#{t+1}")
    for n in range(N):
        number_list.append(list(map(int,input().split())))
    for j in range(N):
        for k in range(N):
            first_line[k] = number_list[N-k-1][j]
            second_line[k] = number_list[N-j-1][N-k-1]
            third_line[k] = number_list[k][N-j-1]
        print(''.join(map(str, first_line)), ''.join(map(str, second_line)), ''.join(map(str, third_line)))


                
                    
                    
    