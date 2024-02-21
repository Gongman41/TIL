def enq(n):
    global last
    last += 1 # 마지막 노드 추가(완전 이진트리 유지)
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last #부모 > 자식 비교를 위해
    p = c//2 # 부모 번호 계산
    while p >=1 and h[p] > h[c]: # 이부분만 수정.부모가 자식보다 값이 더 클 때
        h[p],h[c] = h[c],h[p]
        c = p
        p = c//2 # 바꾸고 한 단 올라가기
def p_search(l):
    p = l//2
    global result
    if not p: #p가 0 아닐 때
        result += h[p]
        return p_search(p)
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    h = [0]*(N+1)
    nodes = list(map(int,input().split()))
    last = 0
    result = 0
    for node in nodes:
        enq(node)
    p_search(last)
    print(f'#{tc} {result}')