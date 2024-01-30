T = int(input())
for tc in range(1,T+1):
    N = int(input())

    def de_multiple(x,y):
        if x%y == 0:
            return 1 + de_multiple(x/y)
        else:
            return 0

    a = de_multiple(N,2)
    b = de_multiple(N, 3)
    c = de_multiple(N, 5)
    d = de_multiple(N, 7)
    e = de_multiple(N, 9)
    print(f"{tc} {a} {b} {c} {d} {e}")



