A,B,W = tuple(map(int,input().split()))
day = 1
if (W-A)%(A-B) == 0:
    day = (W-A)/(A-B)+1
else:
    day = (W-A)//(A-B)+2
print(int(day))
    