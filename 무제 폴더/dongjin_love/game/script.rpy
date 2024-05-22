# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

image class = "images/class.jpg"
image ed = "images/edg.png"
image ed sweet = "images/ed_sweet.png"
image ed umgn= "images/ed_umgn.png"
image ed yoyom= "images/ed_yoyom.png"
image top = "images/top_floor.jpeg"
image chim = "images/chim (2).png"
image chim sweet = "images/chim.png"
image chim youyou = "images/chim_youyou.png"
image last = "images/last.jpg"
# 게임에서 사용할 캐릭터를 정의합니다.
define ed = Character('이동진', color="#e33d05")
define who = Character('??',color="#6b666623")
define chim = Character('이병건',color="#4ec51f98")
define love = 0
define movies = []
define user_name = ''
define user_token = ''
define user = []
default favorite_genres = []
default like_movies = []


define genres = [
    {"pk": 28, "name": "액션"},
    {"pk": 12, "name": "모험"},
    {"pk": 16, "name": "애니메이션"},
    {"pk": 35, "name": "코미디"},
    {"pk": 80, "name": "범죄"},
    {"pk": 99, "name": "다큐멘터리"},
    {"pk": 18, "name": "드라마"},
    {"pk": 10751, "name": "가족"},
    {"pk": 14, "name": "판타지"},
    {"pk": 36, "name": "역사"},
    {"pk": 27, "name": "공포"},
    {"pk": 10402, "name": "음악"},
    {"pk": 9648, "name": "미스터리"},
    {"pk": 10749, "name": "로맨스"},
    {"pk": 878, "name": "SF"},
    {"pk": 10770, "name": "TV 영화"},
    {"pk": 53, "name": "스릴러"},
    {"pk": 10752, "name": "전쟁"},
    {"pk": 37, "name": "서부"}
]

'''
전체 스토리
- 주인공은 평범하게 영화를 좋아하는 고등학교 1학년. 1학기동안 영화부 회장 이동진 선배를 연모하고 있는 상황. 
하지만 얘기해볼 수 있는 기회가 없어 짝사랑만 하고 있었다. 그러다 영화부의 행사를 도와줄 수 있는 기회가 생겨
지원하게 된다. 축제를 도와주면서 이동진 선배와 같이 일할 수 있는 기회가 생기게 되는데..
기승전결. 발단 전개 위기 결말. 영화 질문은 장르, 이동진 평점, 평점, 감독, 배우정도.
장르에 대한 질문으로 장르 가중치를 설정하거나 후속 질문들에는 선행 질문으로 추출된 영화로 질문.
이 게임으로 이 사람의 성향을 전부 다 뽑아낼 필요는 없다. 초기 데이터 수집을 위한 것.

초반엔 가볍게 도와주면서 두근두근 상황. 스몰토크로 데이터 수집. 상황과 관련된 영화? 그냥 아무렇게나 때려넣어도 재밌을 거 같은데
위기가 문제인데. 라이벌 등장? 침착맨, 주호민. 경쟁자 등장.
게임오버는 마지막에만.마지막에 이동진 평점 누적치로 성공여부 출력. 영화 선택 데이터랑 누적치는 서버로 post.


'''
label start:

    show class
    
    $ params = (renpy.emscripten.run_script("get_user_params()"))
    python:
        import json
        user_params = json.loads(params)
    $ user_name = params['username']
    $ user_token = user_params['token']
    
    $ user = renpy.fetch(f"http://127.0.0.1:8000/profile/{user_name}/", method='GET',result="json")
    $ username = user.get("nickname")
    # user.data.get("nickname") 인거 같기도
    $ movies = []
    $ favorite_genres = user.get('like_genre')
    python:
        url = "http://127.0.0.1:8000/api/v1/movieList_for_game/"
        favorite_genres = [str(genre_id) for genre_id in favorite_genres]

        url = url +  "?genre_id=" + "&genre_id=".join(favorite_genres)

    # 왜 갑자기 문자열이 아닌 정수형으로 왔을까.
    $ movies = (renpy.fetch(url, method='GET',result="json"))[:16]
    "나는 대한민국의 평범한 고등학생."

    "외모도, 성적도, 따로 잘하는 것도 없는 평범한 학생이다."

    "그나마 좋아하는 거라고 하면... 영화?"

    "..."

    "선배를 좋아하다보니 닮아버린 걸지도."

    who "어이! 영화부 회장님 오셨다!!"

    who "말씀 한마디 한마디 놓치지말고 잘들으라고!"

    show ed at truecenter
    
    ed "크흠.."

    ed "안녕하세요. 영화부 회장 이동진 입니다."

    ed "저희 동아리 축제를 도와주시러 오셔서 무척이나 감사하고요."

    ed "아무래도 오늘 축제준비는 저희 둘이서 움직일 거 같습니다."

    ed "아 성함을 아직 안물어봤군요."

    ed "숙녀분...신사분...?은 이름이 어떻게 될까요?"


    if username:
        ed "아 [username]씨... 이름 이쁘네요."

        jump start1
    else:
        ed "....네? 잘못들은 거 같은데 다시 말씀해주시겠어요?"

        jump game_over

label start1:

    ed "평소에 영화에 관심이 많으신가봐요. 이렇게 영화부 일도 도와주러 오시고"

    "아... 많이 좋아해요!"

    "(영화도)"

    ed "아하"

    ed "어떤 영화 주로 보세요?"

    menu:
        "[movies[0]['title']]":
            $ like_movies.append(movies[0])
            $ love += movies[0]['dongjin_point']

        "[movies[1]['title']]":
            $ like_movies.append(movies[1])
            $ love += movies[1]['dongjin_point']

        "[movies[2]['title']]":
            $ like_movies.append(movies[2])
            $ love += movies[2]['dongjin_point']

        "[movies[3]['title']]":
            $ like_movies.append(movies[3])
            $ love += movies[3]['dongjin_point']

    if love >= 3.5:
        
        ed "영화를 많이 좋아하시네요."

        ed "[username]씨는 생각보다 더 괜찮으신 분이시군요.."

    else:
        
        ed "그 영화도 괜찮은 영화긴 하죠."

        ed "저랑은 취향이 조금 다르시군요."

    who "선배!! 지금 여기서 뭐하세요!! 바빠죽겠는데!!!"

    who "빨리 옥상에 짐이나 옮겨줘요!!"

    ed "아... 알겠어요."

    ed "[username]씨도 같이 가주시겠어요?"

    menu:
        "물론이죠!":
            
            jump scene1
        "아... 제가 갑자기 몸이 안좋아가...":
            pass


    ed "아.. 네. 알겠습니다."

    ed "...제가 사람을 잘못봤네요."

    jump game_over
    # game_over() 쓰면 어캐되는거지
    return


label scene1:
    scene top
    show ed at truecenter

    ed "날씨가 참 좋네요."

    ed "이런 날씨, 이런 장소에 올라오니 갑자기 한 영화가 떠올라요."

    ed "그 영화를 아실 지 모르겠는데...[username]"

    $ count = 2
    $ check = 0
    python:
        title = max(movies[4:8], key=lambda movie: movie['dongjin_point'])
        title_overview = title['overview'][:80]
    
    while count:
        menu:
            "그 영화 당연히 알죠! [movies[4]['title']]!":
                if movies[4]['title'] == title['title']:
                    $ love += movies[4]['dongjin_point']
                    $ count = 0
                    $ check = 1
                    $ like_movies.append(movies[4])
                else:
                    ed "[title_overview] ..."
                    $ count = count - 1
                    $ like_movies.append(movies[4])
            "그 영화 당연히 알죠! [movies[5]['title']]!":
                if movies[5]['title'] == title['title']:
                    $ like_movies.append(movies[5])
                    $ love += movies[5]['dongjin_point']
                    $ count = 0
                    $ check = 1
                else:
                    $ like_movies.append(movies[5])
                    ed "[title_overview] ..."
                    $ count = count - 1
            "그 영화 당연히 알죠! [movies[6]['title']]!":
                if movies[6]['title'] == title['title']:
                    $ love += movies[6]['dongjin_point']
                    $ count = 0
                    $ check = 1
                    $ like_movies.append(movies[6])
                else:
                    ed "[title_overview] ..."
                    $ count = count - 1
                    $ like_movies.append(movies[6])
            "그 영화 당연히 알죠! [movies[7]['title']]!":
                if movies[7]['title'] == title['title']:
                    $ love += movies[7]['dongjin_point']
                    $ count = 0
                    $ check = 1
                    $ like_movies.append(movies[7])

                else:
                    $ like_movies.append(movies[7])
                    ed "[title_overview] ..."
                    $ count = count - 1
    if  check == 0:
        ed "모를수도 있습니다. 세상에 영화는 많으니까요."

        ed "지금부터 알아가면 되죠."

        ed "이 영화가 재밌는 점은..."

    else:
        ed "아시는군요!! 이 영화가 재밌는 점은..."
        
    "동진선배는 그후로 3시간을 [title['title']]에 대해 얘기했다..."

    "..."

    "선배의 차갑지만 다정한 목소리.."

    "빨간 안경 속 생기 넘치는 눈빛.."

    "지금 이시간이 끝나지 않았으면."

    ed "...한단 말이에요? 그런 측면에서 본다면.."

    who "...탕...탕..."

    who "..선배 마라탕 사주세...탕후루도 같이..."

    show chim:
        xalign 0.1
        yalign 0.6

    chim "선배! 마라ㅌ..."

    chim "..."

    chim "동진쿤. 지금 뭐하는 거야."

    ed "..병건씨."

    "애니부의 이병건."

    "나의 숙적."

    "병건이가 동진선배를 좋아하고 있다는 사실은 학교에서 공공연한 사실이다. "

    "하지만 이렇게 선배가 가버린다면 나는..."

    "에에에에"

    "에에엥에에에에에에에에"
    
    
    menu:
        "푸우엣취[movies[8]['title']]!!!":

            $ like_movies.append(movies[8])

            $ love += movies[8]['dongjin_point']

            python:
                title = movies[8]
                title_overview = title['overview'][:80]
        "푸우엣취[movies[9]['title']]!!!":

            $ like_movies.append(movies[9])

            $ love += movies[9]['dongjin_point']

            python:
                title = movies[9]
                title_overview = title['overview'][:80]
        

        "푸우엣취[movies[10]['title']]!!!":

            $ like_movies.append(movies[10])

            $ love += movies[10]['dongjin_point']
        
            python:
                title = movies[10]
                title_overview = title['overview'][:80]
        "푸우엣취[movies[11]['title']]!!!":

            $ like_movies.append(movies[11])

            $ love += movies[11]['dongjin_point']

            python:
                title = movies[11]
                title_overview = title['overview'][:80]

    ed "!!"
    
    ed "[title['title']]!!!"

    scene top
    show chim:
        xalign 0.1
        yalign 0.7

    show ed yoyom at truecenter
    ed "[title_overview]..."

    ed "그런 지점들이 이 영화에 있다 라고 말씀..."

    ed "...충분히 그렇게 볼수 있을거 같고요 물론 시각적인 측면에선..."

    "시선을 끄는데는 성공했다."

    scene top
    show chim youyou:
        xalign 0.1
        yalign 0.6

    show ed yoyom at truecenter

    chim "선배도 결국."

    chim "한 사람의 남자일 뿐이구나."

    chim "히이이잉!"

    chim "(타다닥 타다닥_계단 내려가는 소리)"

    ed "병건씨!!"

    ed "..."
    scene top
    show chim youyou:
        xalign 0.1
        yalign 0.6
    show ed sweat at truecenter

    ed ".. 이러한 것들 이 영화의 긍정적인 측면을 부각시켜주는 요소란 말이에요. 말하자면 이 영화는 .."

    "(선배는 정말 영화밖에 모르는 바보구나.)"

    "너무 매력적이야."

    "앗 상상으로 한다는 게 입밖으로!"

    ed "..라고 느끼게되는... 네?"

    "아 아니에요."

    "선배 슬슬 내려갈까요? 사람들이 저희 찾고있을 거 같은데.."

    ed "아 그러시죠. 제가 너무 신났네요."

    "(귀여워)"

    jump scene2

label scene2:
    scene last

    "...헉 헉"

    show ed at truecenter

    ed "고생많았어요."

    ed "[username]씨 덕분에 축제 준비가 잘 끝난 거 같아요."

    ed "[username]씨..."

    ed "내일 축제 보러 오실거죠?"

    "(지금이다)"

    "(지금이 아니면)"

    "(선배에게 내 마음을 전할 기회따위)"

    "(있을리가 없어!!!)"

    "'선배에게 고백할 멘트를 선택하세요.'"
    python:
        overview = []
        for movie in movies[12:16]:
            overview.append(movie['overview'][:80])
        
    menu:
        "[overview[0]]...":
            $ like_movies.append(movies[12])
            $ title = movies[12]
            $ love += movies[12]['dongjin_point']

        "[overview[1]]...":
            $ like_movies.append(movies[13])
            $ title = movies[13]
            $ love += movies[13]['dongjin_point']

        "[overview[2]]...":
            $ like_movies.append(movies[14])
            $ title = movies[14]
            $ love += movies[14]['dongjin_point']

        "[overview[3]]...":
            $ like_movies.append(movies[15])
            $ title = movies[15]
            $ love += movies[15]['dongjin_point']

    python:
        import json

        # 기존 사용자 데이터를 가져옴
        pk_list = [movie['id'] for movie in like_movies]
        old_love = user.get('lovepoint', 0)
        old_like_movies = user.get('like_movie', [])

        # 새로운 값 추가
        love = old_love + love
        like_movies = list(set(old_like_movies + pk_list))

        # 새로운 사용자 데이터 생성
        new_user_data = {'lovepoint': love, 'like_movie': like_movies}

        # 새로운 사용자 데이터를 JSON 형식의 문자열로 변환
        new_user_data_json = json.dumps(new_user_data)

        # URL 매개변수로 토큰 전달
        url = f"http://127.0.0.1:8000/profile_for_game/{user_name}/?token={token}"

    $ respond = renpy.fetch(url, method='PUT', data=new_user_data_json, result='json')

    # 응답 상태와 데이터를 로그로 출력

    ed "...!!"

    ed "[title['title']!!]"

    "선배."

    "좋아해요."

    "어쩌면 생각보다 더."

    "매번 도망쳤지만"

    "이제 그만할래."

    "저랑 [title['title']] 보러가요."

    if love >= 13:
        ed "..."

        ed "[username]씨는 정말.."

        scene last
        show ed sweet at truecenter
        ed "멋지네요."

        ed "저의 평론을 이렇게 들어주는 사람은 처음이었습니다."

        ed "[like_movies[0]['title']]도, [like_movies[1]['title']]도, [like_movies[3]['title']]도..."

        ed "같이 봅시다."

        ed "우리."

        "와자뵤"
        jump game_over

    else:
        scene last
        show ed umgn at truecenter
        ed "..."

        ed "[username]씨는 정말 좋은 사람이지만."

        ed "오늘 나눴던 대화에서 이성적인 포인트를 느끼지 못했어요."

        ed "영화 취향도 많이 다른 거 같고..."

        ed "미안하게 됐수다."

        ed "와하하"

        "힝"
    

    jump game_over
    return
# 데이터 가져오기. 캐릭터를 여러 개, 취향도 나눠서...? 아니면 이동진에게 랜덤으로 특정 장르의 영화 데이터를?
label game_over:
    scene ed yoyom
    if love >= 13:
        call screen lovelove_screen
    else:
        call screen game_over_screen
    return

screen lovelove_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("당신은 이동진씨 사랑을 얻게 되었습니다.")
        textbutton _("함 더?") action Return()

screen game_over_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("진짜 게임 개못하네")
        textbutton _("함 더?") action Return()
        