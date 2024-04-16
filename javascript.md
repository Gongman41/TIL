## javascript
- Html script tag
  - 내부는 java script의 영역
- js 확장자 파일
- 브라우저 콘솔

- Dom : 웹페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지구조에 접근할 수 있는 방법을 제공.
  - Dom Api: 페이지 요소들을 객체형태로 제공, 이에 따른 메서드 또한 제공
  - 특징: 트리 구조. 모두 document 객체의 하위객체로 구성.
  - 브라우저는 HTML문서를 해석하여 DOM tree라는 객체트리로 구조화, 객체간 상속 구조가 존재.
  
## document
- 웹페이지 객체
- Don Tree의 진입점
- 이 페이지를 구성하는 모든 객체요소를 표함

## Dom 선택
- 웹페이지를 동적으로 만들기 -> 웹페이지 조작
- 조작하고자 하는 요소 선택 -> 속성 조작
  - document.querySelector('선택자')
    - 처음 만난 element 객체를 반환, 없으면 null 반환
  - document.querySelectorAll('선택자')
    - 선택자가 일치하는 element들을 모아 NodeList 반환
  
## Dom 조작
- 클래스 속성 조작