X,Y = map(int,input().split())
if X == Y:
    print(-1)

    # (Y+a)//(X+a) >= Y//X + 0.01
    # (Y-X)//(X+a) ?= Y//X - 0.99
    # X + a = (Y-X)/((Y/X)-0.99)
elif Y//X == 0.99:
    print(-1)

else:
    Z = (Y-X)//((Y//X)-0.99) - X
    if Z != int(Z):
        print(int(Z)+1)
    else:
        print(int(Z))
