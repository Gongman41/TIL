# def solution(distance, rocks, n):
#     rocks.sort()
#     rocks.append(distance)
#     dt_lst = [[rocks[0],0]].extend([[rocks[i+1] - rocks[i],i+1] for i in range(len(rocks)-1)])
#     dt_lst.sort()
#     # 거리랑 바위위치
    
#     answer = 0
#     return answer

# # 먼저 거리들을 구해놓은다음 최솟값을 계속 찾아서 근처 값이랑 더하고. 근데 매번 다시 정렬해야되는데. 이분탐색을 두번해서 찾고 더하고 빼낸다음 제 위치에 넣고
# #  2, 9, 3, 3, 4, 4
# # 근데 저것도 정렬되어있어야되잖아..
# # 앞에있는 놈 빼서 ... 근데 옆에 있는 놈들 찾는 것도 빡센데.

# 거리로 했구나. 그것도 괜찮은 접근
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left = 1
    right = distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 최소 거리 후보
        prev = 0  # 이전 바위 위치
        removed = 0  # 제거한 바위 수

        for rock in rocks:
            if rock - prev < mid:
                # 거리가 너무 짧으면 제거
                removed += 1
            else:
                prev = rock  # 유지

        if removed > n:
            # 너무 많이 제거함 → 간격이 너무 큼 → 줄이자
            right = mid - 1
        else:
            # 조건 만족 → 간격 늘려보기
            answer = mid
            left = mid + 1

    return answer
