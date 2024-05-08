# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image class = "images/class.jpg"
image ed = "images/edg.png"
# 게임에서 사용할 캐릭터를 정의합니다.
define ed = Character('이동진', color="#e33d05")
define love = 0
python:
    # requests 모듈을 가져옵니다.
    import requests

    # 서버 주소를 설정합니다.
    SERVER_URL = "http://example.com/login"

    # 아이디와 비밀번호를 이용하여 로그인을 시도하는 함수를 정의합니다.
    def authenticate(username, password):
        # POST 요청을 보냅니다. 여기서는 서버로 아이디와 비밀번호를 보냅니다.
        response = requests.post(SERVER_URL, data={"username": username, "password": password})

        # 응답의 상태 코드를 확인하여 로그인 성공 여부를 판단합니다.
        if response.status_code == 200:
            # 서버가 반환한 JSON 응답을 디코딩하여 결과를 확인합니다.
            result = response.json()
            if result["authenticated"]:
                return True
            else:
                return False
        else:
            # 요청에 실패한 경우 False를 반환합니다.
            return False


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
        else:
            ed "....네? 잘못들은 거 같은데 다시 말씀해주시겠어요?"

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


    return
