#비번
class Stack:
    # 스택을 생성할 때 크기를 지정해야 한다
    def __init__(self, size):
        self.size = size # 리스트를 활용해서 구현
        self.data = [None] * size  #값이 없음을 나타내는 None
        self.top = -1 #초기 값이 없으므로 top의 위치는 -1

    def push(self, item):
        if self.is_full():
            print('full')
        self.top += 1
        self.data[self.top] = item

    def get(self):
        return self.data[self.top]

    def __str__(self): #instance print했을 때 stack안의 data를 바로 출력
        return f'{self.data}'

    def pop(self):
        if self.is_empty():
            return -1
        self.top -= 1
        return self.data[self.top+1]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return
import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1,T+1):

    n,st_list = input().split()

    n = int(n)
    prin_stack = Stack(n+1) #프린트할 스택
    for nn in range(n):
        if prin_stack.is_empty() or prin_stack.get() != st_list[nn]:
            prin_stack.push(st_list[nn])
        else:
            prin_stack.pop() #스택 만들기
    print(f'#{tc} ',end = '')
    prin_str = [] #스택 프린트 어떻게하지
    for i in range(prin_stack.top+1): #옮겨담기
        prin_str.append(prin_stack.pop())
    for j in range(len(prin_str)-1,-1,-1):
        print(prin_str[j],end='')
    print()




