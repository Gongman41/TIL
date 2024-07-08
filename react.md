SPA: 하나의 페이지만 존재하는 웹사이트, 웹애플리케이션. content만 여러 개 존재,
Js:동적인 작업을 위해 작성. 
    - 스크립트언어 특징: 런타임에 코드가 해석되고 실행
    - 동적 타이핑
Jsx: 자바스크립트 + XML/HTML
    - React.createElement()를 작성한 것으로 간주
    - React.createElement(
        type,
        [props],
        [...children]
    )
    - 간결, 가독성 향상, injection Attacks 방어
    - xml,html사이 자바스크립트 변수, 함수 참조 {}
    - 상위테그가 하위 태그를 감싸는 식으로하면 자식 작성 가능
    - createReactApp -> 폴더만들기 -> book.jsx 이외에 컴포넌트 작성
    - index.js 수정. import하고 React.StrictMode 안에 넣어줌

Elements: 리액트 앱을 구성하는 가장 작은 블록들
DOM ELEments(많은 정보,브라우저 Dom) <-> ReactElements(가상 Dom)
리액트 Elements는 자바스크립트 객체형태로 존재. 불변성
type:에 문자열이 들어가냐, 그냥 이름이 들어가냐
- Virtual dom에서 수정후 브라우저에 표시

React componet
- props -> react component -> react element
- props: component의 속성, 읽을 수만 있다. 같은 props에 대해서는 항상 같은 결과를 보여줄 것.

함수컴포넌트 -> 훅
- 컴포넌트 = 함수

클래스 컴포넌트
- 함수 컴포넌트 + 상속 React.component

항상 대문자로 시작. 소문자는 dom tag로 인식

component 안에 component 작성 가능
component 추출
