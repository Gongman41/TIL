import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    st_list = input()
    test_list = []
    check = True #걸리면 False
    for st in st_list:
        if st == '{' or st == '(':
            test_list.append(st)
        elif st == '}' or st == ')':

            if test_list == []:#비었는데 추가

                check = False
                break
            elif st == ')':
                if test_list.pop() != '(':#없앤게 짝이 안맞

                    check = False
                    break
            elif st == '}':
                if test_list.pop() != '{':
                    check = False
                    break
    if check == True and test_list == []: #성공적, 안비는 경우 제외
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

