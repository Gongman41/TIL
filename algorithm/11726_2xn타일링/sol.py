n = int(input())

lst = [1,1,2,3]
if n > 3:
    for i  in range(4,n+1):
        lst.append(1)
        for j in range(i-1):
            lst[i] += lst[j]
print(lst[n]%10007)
