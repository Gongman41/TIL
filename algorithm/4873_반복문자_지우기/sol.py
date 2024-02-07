import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    st_list = input()
    test_list = []
    for st in st_list:
        if test_list == [] or test_list[-1] != st: #더하거나 빼거나
            test_list.append(st)
        else:
            test_list.pop()
    print(f'#{tc} {len(test_list)}')

