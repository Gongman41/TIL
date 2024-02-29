T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [0]*401
    for _ in range(N):
        now,comeb = map(int,input().split())
        if (now%2 == 1 and comeb%2 == 0 and comeb == now +1) or (now%2 == 0 and comeb%2 == 1 and now == comeb +1):
            room[now] += 1
            room[comeb] += 1

        elif now > comeb:
            if now%2 == 0 and comeb%2 == 0:
                for i in range(comeb-1,now+1):
                    room[i] += 1
            elif now%2 == 1 and comeb%2 == 0:
                for i in range(comeb-1,now+2):
                    room[i] += 1
            elif now%2 == 1 and comeb%2 == 1:
                for i in range(comeb,now+2):
                    room[i] += 1
            else:
                for i in range(comeb,now+1):
                    room[i] += 1
        else:
            if now % 2 == 0 and comeb % 2 == 0:
                for i in range(now - 1, comeb + 1):
                    room[i] += 1
            elif now % 2 == 1 and comeb % 2 == 0:
                for i in range(now, comeb + 1):
                    room[i] += 1
            elif now % 2 == 1 and comeb % 2 == 1:
                for i in range(now, comeb + 2):
                    room[i] += 1
            else:
                for i in range(now-1, comeb + 2):
                    room[i] += 1
    print(f'#{tc} {max(room)}')
