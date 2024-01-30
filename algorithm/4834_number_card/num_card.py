T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    n_list = list(str(input()))
    temp = [0]*10
    same_c = []
    for n in n_list:
        temp[int(n)] += 1
    max_n = 0
    max_c = max(temp)
    for t in range(len(temp)):
        if temp[t] == max_c:
            same_c.append(t)
    same_c.sort()
    max_n = same_c[len(same_c)-1]

    print(f"#{test_case} {max_n} {max_c}")
