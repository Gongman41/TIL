def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a-1)

N,K = tuple(map(int,input().split()))

print(factorial(N)//(factorial(K)*factorial(N-K)))