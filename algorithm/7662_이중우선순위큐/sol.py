import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []  # 최소 힙 (오름차순 정렬)
    max_heap = []  # 최대 힙 (음수로 저장하여 내림차순 정렬)
    entry = {}  # 유효한 원소를 추적할 딕셔너리

    for _ in range(k):
        command, n = input().split()
        n = int(n)

        if command == 'I':  # 삽입 연산
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            entry[n] = entry.get(n, 0) + 1

        elif command == 'D':  # 삭제 연산
            if n == -1:  # 최솟값 삭제
                while min_heap:
                    min_val = heapq.heappop(min_heap)
                    if entry[min_val] > 0:
                        entry[min_val] -= 1
                        break  # 삭제 성공 시 루프 종료

            elif n == 1:  # 최댓값 삭제
                while max_heap:
                    max_val = -heapq.heappop(max_heap)
                    if entry[max_val] > 0:
                        entry[max_val] -= 1
                        break  # 삭제 성공 시 루프 종료

    # 유효한 원소들만 남기기
    while min_heap and entry[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    while max_heap and entry[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])  # 최댓값, 최솟값 출력
    else:
        print("EMPTY")  # 비어 있으면 EMPTY 출력
