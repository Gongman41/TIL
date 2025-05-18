def solution(genres, plays):
    # 가장 많이 재생된 장르 먼저 -> 그 중에서 가장 많이 재생된 노래 2개, 횟수 같으면 인덱스 빠른 순
    dict_genres = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] in dict_genres:
            dict_genres[genres[i]].append([plays[i],i])
        else:
            dict_genres[genres[i]] = [[plays[i],i]]
  
    plays_genre = []
    for key in dict_genres:
        cnt = 0
        for i in dict_genres[key]:
            cnt += i[0]

        plays_genre.append([cnt,key])
        dict_genres[key].sort(key=lambda x: (-x[0], x[1]))
        # 여기가 킥임. 앞에는 reverse 뒤에는 순차.
    plays_genre.sort(reverse=True)
    
    for genre in plays_genre:
        for i in range(len(dict_genres[genre[1]])):
            answer.append(dict_genres[genre[1]][i][1])
            if i == 1:
                break
    
    
    return answer