N,M,B = map(int,input().split())
t_time = 10e10
t_height = 0
# 블록 제거하는 게 2배 느림. 시간 같으면 높이 큰걸로. 애초에 가지고 있는 블럭 개수.
# 섞어서 써야될수도. 
# while로 백트래킹. 블락 개수가 모자라거나_근데 그럼 부셔서 채우면?_ 최소시간보다 크면 return

mic_n = [list(map(int,input().split())) for _ in range(N)]
for t in range(0,257): # 맞출 높이
    time = 0
    block = B
    for n in range(N):
        for m in range(M):
            if t >= mic_n[n][m]:
                time += t - mic_n[n][m]
                block -= t - mic_n[n][m]
            else:
                time += (mic_n[n][m]-t)*2
                block += mic_n[n][m]-t
            if time > t_time: #이것보다 높은 애들 먼저 제거 후 채우기 실행. 안되면 안되는 거.
                break
        
    else:
        if block >= 0 and time <= t_time:
            t_time = time
            t_height = t
        
print(t_time,t_height)
