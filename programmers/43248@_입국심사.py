def solution(n, times):
    left = 1
    right = max(times) * n  # 최악의 경우 모든 사람이 가장 느린 심사관에게 감
    answer = right

    while left <= right:
        mid = (left + right) // 2  # 현재 시간 후보
        total = sum(mid // t for t in times)  # mid 시간에 처리 가능한 사람 수

        if total >= n:
            answer = mid  # 충분하니까 줄여보기
            right = mid - 1
        else:
            left = mid + 1  # 부족하니까 시간 늘리기

    return answer


# 최소공배수? 각 시험관에 현재 누적시간 갱신?_근데 그럼 계속 정렬 필요_힙?_근데 누가누군지 모름.
# 정해진 시간동안 각 시험관이 몇 명 처리가능한지. 