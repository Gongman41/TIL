T = int(input())

for tc in range(1,T+1):
    K,N,M = tuple(map(int,input().split()))
    st_point_list = list(map(int,input().split()))
    current = 0
    count = 0
    temp_max = 0
    while True:
        arr = False
        for k in range(K):

            current += 1
            if current == N:
                break

            for st_po in st_point_list:
                if current == st_po:
                    temp_max = current
                    arr = True
        if current == N:
            break

        if arr == False:
            count = 0
            break
        else:
            current = temp_max
            count += 1

    print(f'#{tc} {count}')




