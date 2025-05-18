# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     answer = 1
#     cur_wei = weight
#     q = deque([])
#     cur = 0
#     while True:
#         if cur == len(truck_weights):
#             while q:
#                 answer = q.popleft()[0]
#             return answer
#         if cur_wei >= truck_weights[cur]:
#             cur_wei -= truck_weights[cur]
#             q.append([answer + bridge_length, truck_weights[cur]])
#             cur += 1
#             answer += 1
#         else:
#             outmem = q.popleft()
#             cur_wei += outmem[1]
#             answer = outmem[0]

#     # 현재 잔여 무게 변수,여유있으면 deque에서 종료시간을 넣고 없으면 빼고

from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()
    time = 0
    total_weight = 0
    truck_weights = deque(truck_weights)

    while truck_weights or q:
        time += 1

        # 다리에서 나갈 트럭 제거
        if q and q[0][1] == time:
            out = q.popleft()
            total_weight -= out[0]

        # 새 트럭 진입 가능하면 진입
        if truck_weights and total_weight + truck_weights[0] <= weight:
            t_weight = truck_weights.popleft()
            q.append((t_weight, time + bridge_length))  # (무게, 다리에서 나갈 시간)
            total_weight += t_weight

    return time
