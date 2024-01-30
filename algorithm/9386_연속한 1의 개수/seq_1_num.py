T = int(input())
for tc in range(1,T+1):
    N = int(input())
    n_list = list(str(input()))
    seq_n = 0
    max_seq_n = 0
    for n in range(N):
        if int(n_list[n]) == 1:
            seq_n += 1
            if n == N-1:
                if max_seq_n < seq_n:
                    max_seq_n = seq_n


        else:
            if max_seq_n < seq_n:
                max_seq_n = seq_n
            seq_n = 0
    print(f"#{tc} {max_seq_n}")