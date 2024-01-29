N = int(input())
a = [0]*101
n_list = list(map(int(),input().split()))
for n in n_list:
    a[n] += 1

for i in range(100,-1,-1):
    if a[i] != 0:
        a[i] -= 1
        if i == 1
