# def backt(top,value,n):
#     global min_n
#     if top <= value:
#         min_n = min(min_n,value)
#         return
#     for i in range(n):
#         if visited[i] == 0:
#             visited[i] = 1
#             backt(top,value+n_lst[i],n)
#             visited[i] = 0
            
            
T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    # 선반의 높이는 B, 그것보다 같거나 큰 탑중 제일 작은 값
   #그럼 그 경우의 수 중에 B <= x 인데 작은 값을 갱신하면 될 듯
    n_lst = list(map(int,input().split()))
    # #n_lst.sort() 는 다 더해야되는게 아니기 때문에 제외
    # visited = [0]*N
    min_n = 10e10
    # # 차례대로 stack. visited가 문제
    # backt(B,0,N)
    
    # # 제한시간 초과
    
    for i in range(1<<N):
        tem = 0
        for j in range(N):
            if i & (1<<j):
                tem += n_lst[j]
        if tem >= B:
            min_n = min(min_n,tem)
    print(f'#{tc} {min_n-B}')