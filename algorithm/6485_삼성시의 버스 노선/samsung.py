T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bus_list = []
    st_list = []
    count_list = []
    for _ in range(N):
        bus_list.append(tuple(map(int,input().split())))
    P = int(input())

    for _ in range(P):
        st_list.append(int(input()))

    for p in st_list:
        count = 0
        for n in bus_list:
            if p in range(n[0],n[1]+1):
                count += 1
        count_list.append(str(count))

    print(f'#{tc} {" ".join(count_list)}')




