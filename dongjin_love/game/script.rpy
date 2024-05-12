# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image class = "images/class.jpg"
image ed = "images/edg.png"
image top = "images/top_floor.jpeg"

# 게임에서 사용할 캐릭터를 정의합니다.
define ed = Character('이동진', color="#e33d05")
define who = Character('??',color="#6b666623")
define love = 0

init python:
    # requests 모듈을 가져옵니다.
    import requests

    # 서버 주소를 설정합니다.
    SERVER_URL = "http://example.com/login"
    MOVIE_DATA_URL = "http://example.com/movie_data"  # 영화 데이터를 가져올 URL로 변경해야 합니다.

    # 전역 변수로 영화 데이터를 저장할 딕셔너리를 초기화합니다.
    movie_data = {}


    # 아이디와 비밀번호를 이용하여 로그인을 시도하는 함수를 정의합니다.
    def authenticate(username, password):
        # POST 요청을 보냅니다. 여기서는 서버로 아이디와 비밀번호를 보냅니다.
        response = requests.post(SERVER_URL, data={"username": username, "password": password})

        # 응답의 상태 코드를 확인하여 로그인 성공 여부를 판단합니다.
        if response.status_code == 200:
            # 서버가 반환한 JSON 응답을 디코딩하여 결과를 확인합니다.
            result = response.json()
            if result["authenticated"]:
                fetch_movie_data()
                return True
            else:
                return False
        else:
            # 요청에 실패한 경우 False를 반환합니다.
            return False

            # 로그인 성공 시 특정 장르의 영화데이터를 가져오는 로직 작성ㄷ

    

    # 로그인이 성공하면 영화 데이터를 가져와서 전역 변수에 저장하는 함수를 정의합니다.
    def fetch_movie_data():
        global movie_data

        try:
            movie_response = requests.get(MOVIE_DATA_URL)

            # 영화 데이터를 JSON 형식으로 디코딩합니다.
            movie_json = movie_response.json()

            # 가져온 영화 데이터를 전역 변수에 저장합니다.
            movie_data = movie_json

        except Exception as e:
            renpy.say("오류발생!! 오류발생!! 오류발생!!: {}".format(e))


# 여기에서부터 게임이 시작합니다.
label start:

    show class
    show ed at truecenter
    ed "안녕하세요. 전 영화부 회장 이동진 입니다."

    ed "저희 동아리 축제를 도와주시러 오셔서 무척이나 감사하고요."

    ed "아 성함을 아직 안물어봤군요."

    ed "숙녀분...은 이름이 어떻게 될까요?"

    while True:
        call screen input("이름을 입력하세요.") 
        $ username = _return

        call screen input("비밀번호를 입력하세요.") 
        $ password = _return
        # 아이디와 비밀번호 입력. 회원가입은 웹사이트에서 진행
        # 배경이미지는 image 디렉토리에 class.jpg
        # 캐릭터이미지는 edg.png
        if authenticate(username, password):
            ed "아 [username]씨... 이름 이쁘네요."
            jump scene1
        else:
            ed "....네? 잘못들은 거 같은데 다시 말씀해주시겠어요?"

label scene1

    ed "대사를 짜는 건 상당히 어렵군요."

    ed "아직 이동진 그 자체가 되기엔 몰입이 덜 된 거 같습니다."

    ed "일단 가중치 테스트"

    ed "사랑이 뭐라고 생각하시나요?"

    menu:
        "사랑은 번식을 위한 호르몬의 불가해적 행동":
            $ love += 10
                
        "사랑은 가슴의 울렁거림. 인생의 봄이자 여름. 삶의 아리따움.":
            $ love -= 10
        
    if love > 0:
        ed "사랑을 아시는 분."
    else:
        ed "독거노인이 어울리시는 분."
    
    ed "[username]씨는 생각보다 더 괜찮으신 분이시군요.."

    who "선배!! 지금 여기서 뭐하세요!! 바빠죽겠는데!!!"

    who "빨리 옥상에 짐이나 옮겨줘요!!"

    ed "아... 알겠어요."

    ed "[username]씨도 같이 가주시겠어요?"

    menu:
        "물론이죠!":
            $ love += 20
            jump scene2
        "아... 제가 갑자기 몸이 안좋아가...":
            $ love -= 20

    ed "아.. 네. 알겠습니다."

    ed "...제가 사람을 잘못봤네요."

    jump game_over
    # game_over() 쓰면 어캐되는거지
    return


label scene2
    show top
    show ed at center

    ed "날씨가 참 좋네요."

    ed "이런 날씨, 이런 장소에 올라오니 갑자기 한 영화가 떠올라요."

    ed "그 영화를 아실 지 모르겠는데..."

    $ count = 2
    $ check = 0
    while count
        menu:
            "그 영화 당연히 알죠![영화제목1]":
                if 영화제목1 == title:
                    $ love += 20
                    $ count = 0
                    $ check = 1
                else:
                    ed "[description]"
                    $ count -= 1
            "그 영화 당연히 알죠![영화제목2]":
                if 영화제목2 == title:
                    $ love += 20
                    $ count = 0
                    $ check = 1
                else:
                    ed "[description]"
                    $ count -= 1
            "그 영화 당연히 알죠![영화제목3]":
                if 영화제목3 == title:
                    $ love += 20
                    $ count = 0
                    $ check = 1
                else:
                    ed "[description]"
                    $ count -= 1
    if  check == 0:
        ed "모를수도 있습니다. 제가 제 생각에만 또 빠졌군요.."
    else:
        ed "아시는군요!! 이 영화가 재밌는 점은..."
        
        "이동진씨는 그후로 3시간을 [title]에 대해 얘기했다..."
    

    # 영화 설명. descrption을 가져와서 menu로 맞추고 가중치.
    # 아니면 선택지를 주고 맞추면 넘아가고 아니면 description을 주고 맞추기.

    ed
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