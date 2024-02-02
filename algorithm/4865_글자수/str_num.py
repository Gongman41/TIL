import sys
sys.stdin = open("sample_input.txt")
T = int(input())
for tc in range(1,T+1):
    N = input()
    M = input()
    max_c = 0

    for i in N:
        count = 0
        for j in M:
            if j == i:
                count+=1
        max_c = max(count,max_c)
    print(f"#{tc} {max_c}")