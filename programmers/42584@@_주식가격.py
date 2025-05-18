def solution(prices):
    n = len(prices)
    answer = [0] * n  # 정답 리스트
    stack = []  # 인덱스를 저장할 스택

    for i in range(n):
        # 가격이 떨어졌다면 스택에 있는 것들 처리
        while stack and prices[i] < prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top  # 지금(i)에서 떨어진 시점(top)을 빼서 유지 시간 계산
        stack.append(i)

    # 아직 떨어지지 않은 애들 처리
    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top  # 끝까지 안 떨어졌으면 전체 시간 계산

    return answer

# time 변수 따로 두고 지금보다 큰지 안큰지는 스택으로.