web: web site등을 통해 사용자들이 정보를 검색하고 상호작용하는 기술
web site: 인터넷에서 여러 개의 web page 가 모인 것으로 사용자들에게 정보나 서비스를 제공하는 공간
web page: HTMP,CSS등의 웹 기술을 이용하여 만들어진 웹사이트를 구성하는 하나의 요소
  - structure: HTML_웹페이지의 의미과 구조를 정의하는 언어
   - Hypertext: 링크. 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
   - Markup Language: 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어. 이쁘게 ㅇㅇ
   - 구조
    - <!DOCTYPE html> :해당 문서가 html로 문서라는 것을 나타냄
    - <html></html>: 전체 페이지의 콘텐츠를 포함. 여는 태그, 닫는 태그
    - <title></title>: 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
    - <head></head>: HTML 문서에 관련된 설명,설정등. 사용자에게 보이지 않음
    - <body></body>: 페이지에 존재하는 모든 콘텐츠.
    이를 확인하기 위해선 개발자 도구를 켜보면됨
    - HTML Element
      - 여는 태그와 닫는 태그, 그리고 그 안의 내용으로 구성. 닫는 태그는 태그 이름앞에 / 포함
        닫는 태그가 없는 태그도 존재
    - HTML Attributes
      - 규칙
        - 속성은 요소 이름과 속성사이의 공백이 있어야 함
        - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
        - 속성 값은 열고 닫는 따옴표로 감싸야함
      - 목적
        - 나타내고 싶지않지만 추가적인 기능,내용을 담고 싶을 때 사용
        - CSS에서 해당 요소를 선택하기 위한 값으로 활용
    - 의미 생성
      - 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여
    MDN Web Docs


  - styling: CSS_ 웹 페이지의 디자인과 레이아웃을 구성하는 언어
    - Casading Style sheet_아래로 흐르는
      - 선택자(h1): HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자
        - 기본선택자
          - * 전체 선택자
          - 요소(tag)선택자
          - 클래스 선택자
          - 아이디 선택자: 문서에는 주어진 아이디를 가진 요소가 하나만 있어야함
          - 속성 선택자

        - 결합자
          - 자손 결합자(space)
            - 첫번째요소의 자손요소들 선택
          - 자식 결합자(>)
            - 첫번째 요소의 직계 자식만 선택(한단계 아래 자식들만)
      - 선언({})_ 끝날 때마다 세미콜론
      - 속성
      - 값
    - 내부,외부 스타일 선언방식 선호
    - 명시도: 결과적으로 요소에 적용할 css선언을 결정하기 위한 알고리즘
      선택자에 가중치 계산. 높은 명시도를 가진 선택자가 승리.
      동일한 가중치를 가졌을 때 마지막에 나오는 선언이 사용
      - importance > inline style > id > class > 요소 > 소스코드 선언 순서
    - 속성은 되도록 class만 사용할 것
    - CSS 상속: 상속되는 속성_텍스트 관련, 안되는 속성 존재(배치 관련)
  
  - behavior: javascript

## CSS Box Model
- 모든 HTML 요소를 사각형 박스로 표현하는 개념_원은 네모 박스를 깎은 것
- 내용(content),안쪽여백(padding)_내용과 테두리 사이,테두리(border), 외부간격(margin)
- 방향 - top,bottom,left,right
- 안쪽 내용은 width와 height로 표현_ width는 content 영역의 너비. 테두리 기준 x.
  {
    box sizing: border-box
  }
- 박스타입
- 블록: 막음_ 오른쪽을 다 막고 있기때문에
  - 아래로 
  - 항상 새로운 행으로 나뉨
  - 너비와 높이 지정가능
  - width 지정하지 않으면 inline 방향으로 사용가능한 공간 모두 차지함
  - h1-6 p div
- 인라인: 어디 들어감
  - 좌측에서 오른쪽으로
  - 새로운 행으로 나뉘지 않음
  - width,height 지정 불가_ 콘텐츠만큼만.(이미지만 제외)
  - 수직방향_ padding, margins, borders 적용, 하지만 다른 요소를 밀어낼 수는 없음
  - 수평방향_ padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
  - a,img,span
- 속성에 따른 수평정렬
  - block: margin으로
  - inline: text-align
- 기타 display 속성
  - inline-block: 기본적으로 inline. 너비와 높이, 요소를 위아래로 미는 것 추가
    - 줄바꿈을 원하지 않으면서 너비와 높이를 적용하고싶은 경우에 사용
  - none: 사라져볼게. 화면 크기별로 레이아웃 바꿀때_ 반응형 레이아웃
shorthand:margin.padding
  - 4개_상하좌우, 3개_상 좌우 하,2개_상하 좌우,1개_ 공통
margin collapsing(마진상쇄)
  - 두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상
  - 웹 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함
  - 한 요소에 대해서만 설정
  - 좌우는 아님
## CSS Position
- css layout: 각 요소의 위치와 크기를 조정하여 웹페이지의 디자인을 결정하는 것
- css position: 각 요소를 Normal flow에서 제거하여 원하는 위치에 배치
- 유형
  - static: 기본위치
  - relative: 자신의 static위치에 밀어서 반대방향으로 이동. 본인이 이동을 하더라도 과거 위치는 그대로 존재. 마치 두개 존재하는 느낌
  - absolute: 본인의 영역 버리기_ 레이아웃 깨질 위험. 이동을 하려면 새로운 기준점_static이 아닌 가장 가까운 부모_부모를 relative로 바꿔줘야됨
    - 왜 relative인가.부모 이동하면 따라가야됨
  - fixed: 본인의 영역 버리기. 화면기준으로 고정_ 스크롤해도 변경 x.
  - sticky: 일단 Normal flow. 스크롤이 특정 임계점 되면 fixed. top이 0이 될 때 처럼
  - z-index: 요소가 겹쳤을 떄 어떤 요소 순으로 보이게 할 것인가. 
    - 더 큰 값이 앞으로 나옴. 값을 안주면 일단 순서대로
- position의 역할: 전체 페이지에 대한 레이아웃을 조정하는 게 아닌 특정 위치의 

## CSS Flexbox
- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식_공간배열, 정렬
  - Flex Container: display:flex; 혹은 display: inline-flex가 설정된 부모요소
    - Flex Item
  - cross axis: main axis에 수직인 축.위에서 아래가 기본값.
  - main axis : flex item들이 배치되는 기본 축.왼쪽에서 오른쪽이 기본값
    - main start, main end 바꿔서 순서 바꿀 수 있음
  - flex-direction
  - flex-wrap: 요소들 크기 유지하고 싶을 때 설정. 밑으로 떨어짐
  - justify-content: 주 축을 따라 flex item과 주위에 공간을 분배
    - 마진 넣고 염병 안떨어도 됨
  - align-content: 여러 줄을 교차축에 따라 분배
    - flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용
    - 한줄 짜리 행에는 효과 없음
  - align-items: 한줄정렬. 두 줄되는 순간 안됨. wrap하면 안됨
  - align-self: 하나하나 따로 움직일 때
  - flex-grow: 남는 행 여백을 flex items의 비율에 따라 배분. 해서 애들한테 준거. 그 비율만큼 요소의 크기 정해지는 거 아님. 그냥 준거
  - flex-basis: 요소의 초기 크기값 지정. width 같이 한 경우 flex-basis가 우선
  목적에 따른 속성 분류
  - 배치: flex-direction, flex-wrap
  - 공간분배: justify-content, align-content
  - 정렬: align-items, align-self
  속성명 tip
  - justify_주 축, align_교차축
  - content_ 여러줄, items_한 줄, self_요소 한 개

  - justify-items,self 속성이 없는 이유: 필요 없기 때문. margin auto를 통해 정렬 및 배치가 가능