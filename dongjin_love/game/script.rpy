# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image class = "images/class.jpg"
image ed = "images/edg.png"
image ed sweet = "images/edg_sweet.png"
image ed umgn= "images/edg_umgn.png"
image ed yoyom= "images/edg_yoyom.png"
image top = "images/top_floor.jpeg"
image chim = "images/chim (2).png"
image chim sweet = "image/chim.png"
# 게임에서 사용할 캐릭터를 정의합니다.
define ed = Character('이동진', color="#e33d05")
define who = Character('??',color="#6b666623")
define chim = Character('이병건',color="#4ec51f98")
define love = 0
define movies = []
define username = ''
default favorite_genres = []
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
    
    $ user_name = (renpy.emscripten.run_script_string("get_user_name()")).replace("\\'", "'")
    
    $ user = (renpy.fetch(f"http://127.0.0.1:8000/profile/{user_name}/", method='GET',result="json"))
    $ username = user.get("nickname")
    # user.data.get("nickname") 인거 같기도
    $ movies = []
    $ favorite_genres = user.get('like_genre')
    $ like_movies = []
    python:
        url = "http://127.0.0.1:8000/api/v1/movieList_for_game/"
        url = url +  "?genre_id=" + "&genre_id=".join(favorite_genres)


    $ movies = (renpy.fetch(url, method='GET',result="json"))[:20]
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
            
            jump scene2
        "아... 제가 갑자기 몸이 안좋아가...":
            pass


    ed "아.. 네. 알겠습니다."

    ed "...제가 사람을 잘못봤네요."

    jump game_over
    # game_over() 쓰면 어캐되는거지
    return


label scene2:
    scene top
    show ed at truecenter

    ed "날씨가 참 좋네요."

    ed "이런 날씨, 이런 장소에 올라오니 갑자기 한 영화가 떠올라요."

    ed "그 영화를 아실 지 모르겠는데...[username]"

    $ count = 2
    $ check = 0
    python:
        title = max(movies[4:8], key=lambda movie: movie['dongjin_point'])
    while count:
        menu:
            "그 영화 당연히 알죠! [movies[4]['title']]!":
                $ like_movies.append(movies[4])

                if movies[4]['title'] == title['title']:
                    $ love += movies[4]['dongjin_point']
                    $ count = 0
                    $ check = 1
                else:
                    ed "[title['overview'] ...]"
                    $ count -= 1
            "그 영화 당연히 알죠! [movies[5]['title']]!":

                $ like_movies.append(movies[5])

                if movies[5]['title'] == title['title']:
        
                    $ love += movies[5]['dongjin_point']
                    $ count = 0
                    $ check = 1
                else:
                    ed "[title['overview'] ...]"
                    $ count -= 1
            "그 영화 당연히 알죠! [movies[6]['title']]!":
                $ like_movies.append(movies[6])

                if movies[6]['title'] == title.get('title'):
                    $ love += movies[6]['dongjin_point']
                    $ count = 5
                    $ check = 1
                else:
                    ed "[title['overview'] ...]"
                    $ count -= 1
            "그 영화 당연히 알죠! [movies[7]['title']]!":
                $ like_movies.append(movies[7])

                if movies[7]['title'] == title.get('title'):
                    $ love += movies[7]['dongjin_point']
                    $ count = 0
                    $ check = 1
                else:
                    ed "[title['overview'] ...]"
                    $ count -= 1
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

    who "..선배 마라탕 어쩌구저쩌구...탕후루도 같이 어쩌구"

    show chim:
        xalign 0.2
        yalign 0.5

    chim "선배! 마라ㅌ..."

    chim "..."

    chim "동진선배. 지금 뭐하는 거야."

    ed "..병건씨."

    "애니부의 이병건."

    "나의 숙적."

    "병건이가 동진선배를 좋아하고 있다는 사실은 학교에서 공공연한 사실이다. "

    "하지만 이렇게 선배가 가버린다면 나는..."

    "에에에에"

    "에에엥에에에에에에에에"
    
    
    menu:
        "푸우엣[movies[8]['title']]!!!":

            $ like_movies.append(movies[8])

            $ love += movies[8]['dongjin_point']

            $ title = movie[8]
        "푸우엣[movies[9]['title']]!!!":

            $ like_movies.append(movies[9])

            $ love += movies[9]['dongjin_point']

            $ title = movie[9]
        

        "푸우엣[movies[10]['title']]!!!":

            $ like_movies.append(movies[10])

            $ love += movies[10]['dongjin_point']
        
            $ title = movie[10]

        "푸우엣[movies[11]['title']]!!!":

            $ like_movies.append(movies[11])

            $ love += movies[11]['dongjin_point']

            $ title = movie[11]

            
    ed "[title['title']]!!!"

    scene top
    show chim:
        xalign 0.2
        yalign 0.5
    show ed yoyom at truecenter
    ed "[title['overview']]..."

    ed "그런 지점들이 이 영화에 있다 라고 말씀..."

    ed "충분히 그렇게 볼수 있을거 같고요 물론 시각적인 측면에선..."

    "시선을 끄는데는 성공했다."

    
    
        




    # 영화 설명. descrption을 가져와서 menu로 맞추고 가중치.
    # 아니면 선택지를 주고 맞추면 넘아가고 아니면 description을 주고 맞추기.

    ed "엔딩 테스트"

    jump game_over
    return
# 데이터 가져오기. 캐릭터를 여러 개, 취향도 나눠서...? 아니면 이동진에게 랜덤으로 특정 장르의 영화 데이터를?
label game_over:
    if love >= 50:
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
        