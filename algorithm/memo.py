N,M = map(int,input().split())
check = True
for n in range(N):
    if not (M & (1<<n)):
        check =False
if check == True:
    print('ON')
else:
    print('OFF')