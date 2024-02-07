class Node:
    def __init__(self,data,target=None):
        self.data = data
        self.target = target
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False
    def enqueue(self,data,target=0):
        new_node = Node(data,target)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            dequeued = self.front
            self.front = self.front.next

        if self.front is None:
            self.rear = None
        return dequeued

    def peak(self):
        if self.isEmpty():
            return -1
        else:
            return self.front
import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
    queue = Queue()
    N,M = map(int,input().split())
    n_list = list(map(int,input().split()))
    for n in range(N):
        if n == M:
            queue.enqueue(n_list[n],1)
        else:
            queue.enqueue(n_list[n])
    n_list.sort()
    count = 0
    while not queue.isEmpty():
        if n_list[-1] == queue.peak():
            if queue.front.target == 1:
                count += 1
                print(count)
                break
            else:
                n_list.pop()
                queue.dequeue()
                count += 1
        else:

            queue.enqueue(queue.dequeue().data,queue.dequeue().target)

























