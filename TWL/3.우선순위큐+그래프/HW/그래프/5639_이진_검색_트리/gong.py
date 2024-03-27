import sys
sys.stdin = open('input.txt')
nodes = {}
nodes[1] = [int(input()),0,0,0]
cur = 1
while True:
    try:
        a = int(input())
        if a <= nodes[cur][0]:

            nodes[cur*2] = [a,cur,0,0]
            nodes[cur][2] = 2*cur

            cur *= 2
        else:
            while cur != 1:
                if nodes[cur//2][0] > a:

                    nodes[2*cur+1] = [a,cur,0,0]
                    nodes[cur][3] = 2*cur+1
                    cur = cur * 2 + 1
                    break
                else:
                    cur //= 2
            else:
                cur =3
                nodes[cur] = [a,1,0,0]
                nodes[1][3] = 3
    except EOFError:
        break

def last(start):
    if nodes.get(start,0) == 0:
        return

    last(start*2)
    last(start*2+1)
    print(nodes[start][0])

last(1)

#         왼쪽 자식인 경우, 오른쪽 자식인 경우
#  형제인 경우
# 조상의 형제인 경우
# 입력머ㅏㅁ추기