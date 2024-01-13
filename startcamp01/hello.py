t = int(input())

for i in range(t):
    a = input()
    n = list(map(int, a.split()))  

    max_n = 0
    
    for j in n:
        if j > max_n:
            max_n = j

    print(f"#{i+1} {max_n}") 