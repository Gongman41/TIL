T = int(input())
for tc in range(1,T+1):
    N,Q = map(int,input().split())
    n_boxes = [0]*N
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for j in range(L-1,R):
            n_boxes[j] = i
    print(f"#{tc} {' '.join(map(str, n_boxes))}")


