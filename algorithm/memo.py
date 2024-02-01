N, K = map(int, input().split())
share_ncard = list(map(int, input().split()))
team_ncard = list(map(int, input().split()))

max_n_list = []
for s in range(len(share_ncard)):
    for t in range(len(team_ncard)):
        max_n_list.append([share_ncard[s] * team_ncard[t], t])
max_n_list = sorted(max_n_list, key=lambda x: x[0])
for k in range(K):
    a = max_n_list.pop()
    team_ncard.pop(a[1])
    i = 0
    while i != len(max_n_list):
        if max_n_list[i][1] == a[1]:
            max_n_list.pop(i)
        else:
            i += 1

print(max(team_ncard) * max(share_ncard))









