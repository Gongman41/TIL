def solution(progresses, speeds):
    answer = []
    cur = 0
    for i in range(101):
        cnt = 0
        while progresses[cur] + i >= 100:
            cnt += 1
            cur += 1
            if cur == len(progresses):
                return answer
        if cnt != 0:
            answer.append(cnt)
            