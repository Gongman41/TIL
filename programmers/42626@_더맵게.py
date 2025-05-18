from heapq import heappush, heappop, heapify

def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while scoville:
        # 가장 작은 값이 K 이상이면 끝
        if scoville[0] >= K:
            return answer

        # 더 섞을 재료가 부족한 경우
        if len(scoville) < 2:
            return -1

        # 가장 맵지 않은 두 개 꺼내서 섞기
        first = heappop(scoville)
        second = heappop(scoville)
        new_scoville = first + second * 2
        heappush(scoville, new_scoville)
        answer += 1

    return -1
