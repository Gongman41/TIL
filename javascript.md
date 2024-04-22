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
  
### NodeList
- DOM의 변경사항 실시간으로 반영하지 않음

## syntax
- 변수 선언 키워드
  - 반드시 문자,$,_ 로 시작
  - 대소문자 구분
  - 예약어 (for,if) 사용 불가

- 종류
  - let
    - 블록스코프(중괄호 내부, 블록 바깥에서 접근 불가능)를 갖는 지역변수 선언
    - 재할당 가능
    - 재선언 불가능(선언 키워드 있나 없냐)
    - ES6에서 추가

  
  - const
    - 블록스코프 지역변수 선언
    - 재할당 불가능
    - 재선언 불가능 (상수기때문)
    - ES6에서 추가
    - 선언 시 반드시 초기값 설정 필요
  기본적으로 const 사용. 재할당 필요 시 let으로 사용

  - var

- 식별자
  - 카멜케이스: 변수, 객체, 함수에 사용
  - 파스칼 케이스: 클래스, 생성자에 사용
  - 대문자 스네이크 케이스: 상수에 사용
  
- 데이터 타입
  - 원시 자료형: 변수에 값이 직접 저장되는 자료형(불변, 값이 복사)
                변수 간에 서로 영향을 미치지 않음
    - Number: 정수 또는 실수형 숫자를 표현하는 자료형
      - NaN: not a number_숫자로 표현 불가
    - String: 문자열. +로 결합 가능. 다른건 불가
      - 템플릿 리터럴: 문자열안에 변수같은거 넣기. 백틱 사용. ${expression} 으로 표기 엔터도 인식
    - Boolean: true, false 유의. 자동형변환 적용.
    - null: 변수의 값이 없을을 의도적으로 표현
    - undefined: 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당
  - 참조 자료형: 객체의 주소가 저장되는 자료형(가변,주소가 복사)
              변수간에 서로 영향을 미침. 파이썬의 리스트, 딕셔너리 할당과 비슷

- 연산자
  - 할당연산자_단축 연산자 지원  
  - 증가, 감소 연산자: 뒤에 붙이면 이번 표현식 끝나고 증가. 앞에는 지금 바로.
  - 비교 연산자
  - 동등연산자: 암묵적 타입 변환(문자열과 정수형, 정수형과 불리언,객체간 비교 가능)
    - null, undefined 같은 경우에 사용하기도
  - 일치 연산자(===): 값과 타입 모두 같은 경우. 사용 권장
  - 논리 연산자 &&, ||, !, 단축평가 지원

- 조건문
  - if: (조건) {참일 시 표현식}
  - 삼항연산자: condition ? expression1(true일경우) : expression2(false일 경우) 

- 반복문
  - while (조건문) {}
  - for (초기문; 조건문; 증감문;){}
  - for... in 객체(순서가 없음), 속성을 출력 , 반복가능한 객체를 넣으면 인덱스가 나옴, 순서를 보장하지 않음
  - for ... of 반복가능한 객체(순서가 있는). 순서가 중요한 배열에서 사용

  - 반복문 사용 시 const 사용 여부: for in , for of 는 매 반복마다 다른 속성 이름이 변수에 지정. 블록 내부에서 변수 수정 불가. 바꿀거면 let으로 변경

- 세미콜론 자동으로 삽입. 선택적으로 사용가능
- 호이스팅: 변수 선언 이전에 참조. undefined 출력
- 변수선언 키워드 없이 선언 시 자동으로  var 적용
- NaN 반환 예시
  - 숫자로서 읽을 수 없음
  - 결과가 허수인 수학 계산식
  - 피연산자가 NaN
  - 정의할 수 없느 ㄴ계산식
  - 문자열을 포함하면서 덧셈이 아닌 계산식
  
## Reference Type
- 함수: 참조 자료형(가변, 주소가 복사), 모든 함수는 function object
  - 종류
    - objects
    - Array
    - Function
  - 정의
    - function name ([param[param...]]) {
      statements
      return value
      }
      리턴 없으면 undefined
    - 선언식은 위
    - 표현식(익명함수 사용가능, 사용 권장)
      - const funcName = function (){
        }
      - 사용하는데는 차이 없음
      - 호이스팅이 되지않음_함수 정의전에 사용 불가
  - 매개 변수
    - 기본 함수 매개변수
      - 전달하는 인자가 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화
    - 나머지 매개변수
      - 임의의 수의 인자(가변인자)를 배열로 허용하여 가변인자를 나타내는 방법
      - const myFunc = function(param1,param2,...restParams)
      - 없으면 빈 비열로 묶임
      - 함수정의에서 마지막에 한번만 작성 가능.
      - 매개변수의 개수와 인자 개수가 불일치할 때 누락된 인자 undefined로 할당
        - 초과된 인자는 사용하지 않음
    - spread syntax(전개구문): '...' 배열이나 문자열과 같이 반복가능한 항목을 펼치는 것
      - 전개 대상에 따라 역할이 다름
      - 함수와의 사용
        - 함수 호출 시 인자 확장_언패킹 느낌
        - 나머지 매개변수(압축)
  - 화살표 함수 표현식
    - const arrow = name => 'hello, ${name}'
    - function 키워드 제거 후 매개변수와 중괄호 사이에 화살표 작성
    - 매개변수가 하나뿐이라면 매개변수의 소괄호 제거 가능(그냥 생략 안하는 거 추천)
    - 본문의 표현식이 한 줄이라면 {} 와 return 제거가능
    - 심화
      - 인자가 없으면 () or _ 로 표시 가능
      - 객체 리턴 시 return 명시적으로 작성
        - 리턴 안쓸거면 객체를 소괄호로 감싸
- 객체: 키로 구분된 데이터 집합을 저장하는 자료형
  - 구조 및 속성
    - 중괄호를 이용해 작성
    - 중괄호 안에는 키 밸류쌍으로 구성된 속성을 여러개 작성 가능
    - key는 문자형만 허용( 공백없으면 따옴표 생략가능)
    - value는 모든 자료형 허용
    - value자리에 함수있으면 메서드
  - 속성 참조
    - . , [] 로 객체 요소 접근
    - key 이름에 띄어쓰기같은 구분자 있으면 대괄호 접근만 가능
    - 속성 추가시 user.address = 'korea' 이런 식. 이미 있으면 수정
    - 삭제시 delete user.name
  - in 연산자: 속성이 객체에 존재하는지 여부를 확인(key를 확인)
  
  - 객체와 함수
    - Method: 객체의 속성으로 존재하는 함수
    - object.method() 방식으로 호출
    - 메서드는 객체를 '행동'할 수 있게 함
    - this: 함수나 메서드를 호출한 객체를 가리키는 키워드
      - 단순 호출: 전역 객체
      - 메서드 호출: 메서드를 호출한 객체
      - 호출하는 방법이 중요
      - self랑은 다르다. 무조건 자기자신이지는 않음
      - forEach의 인자같이 단순호출되면 전역
        - 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부함수에서의 thist 값을 가져옴
      - 호출 시 암묵적으로 전달받음
      - 함수 호출 시 값이 할당(동적 할당) <-> 파이썬의 self, 자바의 this는 선언 시 값이 정해짐 
        - 여러 객체에서 사용가능, but 실수 발생 가능
  - 추가 객체 문법
    - 단축 속성: 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우
      - name: name -> name
    - 단축 메서드: ': function' 생략가능
    - 계산된 속성: 키가 대괄호로 둘러싸여있는 속성_ 고정된 값이 아닌 변수값 사용가능
    - 구조 분해 할당: 함수의 매개변수로 활용가능, import 시에도
    - 전개구문 with object: 객체 복사_ 얕은 복사
    - 유용한 객체 메서드
      - object.keys()
      - object.values()
    - optional chaining: 속성이 없는 중첩객체를 에러없이 접근하는 방법 
      - 참조 대상이 null 또느 ㄴundefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined 반환 (?.)
      - 안쓰면 && 사용해서 처리
        - 편리한 탐색, 간단한 표현식
        - 존재하지 않아도 괜찮은 대상에만 사용
        - optional chaining 앞의 변수는 반드시 선언
  - JSON
    - 객체처럼 생겼지만 문자열
    - 변환하는 과정 필요_ 자바스크립트에서는 객체로.
```javascript
// Object -> JSON
    const objToJson = JSON.stringify(jsObject)
    console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
    console.log(typeof objToJson)  // string

    // JSON -> Object
    const jsonToObj = JSON.parse(objToJson)
    console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
    console.log(typeof jsonToObj)  // object
```
  - new: 함수로 생성자 만든다음 앞에 new를 붙여 변수에 할당
- 배열
  - Array: 순서가 있는 데이터 집합을 저장하는 자료구조
    - length 속성을 이용해 배열에 담긴 요소가 몇개인지 알 수 있음
    - 대괄호를 이용해 작성
    - 메서드
      - push, pop_반환 후 제거
      - unshift,shift: 앞쪽 추가, 제거 후 반환
    - array helper method
      - 배열의 각 요소를 순회, 각 요소에 대해 함수_콜백함수를 호출
      - 메서드 호출 시 인자로 함수(콜백함수)를 받는 것이 특징
        - 콜백함수: 다른 함수에 인자로 전달되는 함수
          - 외부함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행
      - forEach : 배열 내의 모든 요소 각각에 대해 함수를 호출,반환값 없음 
        - item_필수요소, index_처리할 배열요소 인덱스(선택), array(선택인자)
        - 반환값: undefined
        - 화살표 함수 표시
        - 이게 제일 좋음
      - map: 배열 내의 모든 요소 각각에 대해 함수를 호출, foreach+ 새로운 배열 
      - some, every
      - 반환,ewru

# Controlling event
## 이벤트
- 웹에서의 모든 동작은 이벤트 발생과 함께 한다
- event object: Dom에서 이벤트가 발생했을 때 생성되는 객체
  - mouse, input,keyboard...
  - Dom요소는 event를 받고 받은 event를 처리(event handler)할 수 있음
- event handler: 이벤트가 발생했을 때 실행되는 함수
  - .addEventListener(): 대표적인 이벤트 핸들러 중 하나(콜백함수_인자로도 함수를 받음)
  - 특정 이벤트를 DOM요소가 수신할 때마다 콜백함수를 호출
  - EventTarget(Dom요소).addEventListener(type(수신할 이벤트),handler(콜백함수))
    - 대상에 특정Event가 발생하면 지정한 이벤트를 받아 할일을 등록한다
    - type : 수신할 이벤트 이름, 문자열로 작성\
    - handler: 발생할 이벤트 객체를 수신하는 콜백함수, 발생한 event object를 유일한 매개변수로 받음
- ex) 버튼 클릭 시 / 버튼 요소 출력하기
```js
// 버튼 선택
const btn = document.querySelector('#btn')
// 콜백함수_반환값 없음. event 객체를 유일한 매개변수로
const detectClick = function (event )  {
  console.log(event)
  console.log(this)
  // this = btn. 위 아래는 사실 같은 코드
  console.log(event.currentTarget)
// 속성 개많음_PointerEvent
}
// btn.addEventListener('click',function(event) {
//   console.log(event)
//   console.log(this)
//   // this = btn
//   console.log(event.currentTarget)
// // 속성 개많음_PointerEvent
// })
// 버튼에 이벤트 핸들러를 부착
btn.addEventListener('click',detectClick)
```
- 내부의 this값은 대상요소(event객체의 currentTarget 속성값과 동일)
- 버블링: 중첩된 구조에 각각 이벤트 핸들러가 있을 때. 가장 내부 선택시 차례대로 출력_ 부모요소의 핸들러가 동작, 최상단 조상요소까지.
  - 하위요소에 연결 안되어있어도 버블링되서 연결되어있는 곳에서 핸들러
  - 이벤트가 정확히 어디서 발생했는 지 접근할 수 있는 방법
    - event.currentTarget: 현재요소, 이벤트 핸들러가 연결된 요소만을 참조, this와 같음, 불변
    - event.target: 이벤트가 발생한 가장 안쪽의 요소를 참조, 실제 이벤트가 시작된 요소, 버블링이 진행되어도 변하지 않음, 가변
  - 버블링이 필요한 이유: 각자 다른 동작 수행하는 버튼 짱많으면 target,currentTarget으로 해야 하나하나 설정 안해도 됨
- 캡쳐링: 이벤트가 하위요소로 전파되는 단계(버블링과 반대)

- 버튼 클릭 시 숫자 1씩 증가해서 출력
```js
// 3.초기값 선언
let count = 0
// 1.버튼 선택
const btn = document.querySelector('#btn')
// 2. 함수 작성
const clickHandler = function() {
  // 3.1 초기값 1 증가
  count += 1
  // 2.1 카운트할 요소 선택
  const spanTag = document.querySelector('#counter')
  // 2.2 카운트할 요소 안에 숫자를 선택_그냥 숫자가 할당됨. 
  // let counterNumber = spanTag.textContent
  
  // 3.2 증가된 숫자를 counterNumber에 재할당
  // counterNumber = count
  spanTag.textCount = count
}
// 4. 이벤트 핸들러 부착
btn.addEventListener('click',clickHandler)
```
- 사용자의 입력값을 실시간으로 출력
```js
// 1. input 태그 선택
const inputTag = document.querySelector('#text-input')
// 3.2 p 태그 선택
const pTag = document.querySelector('p')
// 2. 콜백함수
const inputHandler = function(event) {
  // 3.1 작성하는 데이터가 어디에 누적되고 있는지 찾기
  // console.log(event)
  // console.log(this.value)
  // console.log(event.currentTarget.value)
  // 3.3 사용자 입력 데이트럴 p 태그의 컨텐츠로 저장
  pTag.textContent = event.currentTarget.value
  // 누적시키거나 한방에 접근하거나
} 
// 4. 선택한 input 태그에 이벤트 핸들러 부착
inputTag.addEventListener('input',inputHandler)
```
  - currentTarget 주의사항: 버블링 순서때문에 console에서 null값
- + '+'버튼을 클릭하면 출력한 값의 css스타일을 변경하기


```js
// 1. input 태그 선택
const inputTag = document.querySelector('#text-input')
const h1Tag = document.querySelector('h1')
const btn = document.querySelector('#btn')
// 2. 콜백함수
const inputHandler = function(event) {

  h1Tag.textContent = event.currentTarget.value
} 

const clickHandler = function() {
  // add 방법
  // h1Tag.classList.add('blue')
  // toggle 방법
  h1Tag.classList.toggle('blue')
// if 방법
  // if (h1Tag.classList.value){
  //   h1Tag.classList.remove('blue')
  // } else {
  //   h1Tag/classList.add('blue')
  // }

}

// 3. 선택한 input 태그에 이벤트 핸들러 부착
inputTag.addEventListener('input',inputHandler)
btn.addEventListener('click',clickHandler)
```


- todo 프로그램 구현
```js
const inputTag = document.querySelector('.input-text')
// 클래스
const btn = document.querySelector('#btn')
const ulTag = document.querySelector('ul')

const addTodo = function (event) {
  // event.currentTarget = btn
  const inputData = inputTag.value
  if (inputData.trim()) {
    // trim은 공백제거 메서드
  // li 태그 생성
  const liTag = document.createElement('li')
  liTag.textContent = inputData
  ulTag.appendChild(liTag)
  // todo 추가 후 input의 입력 데이터는 초기화
  inputTag.value = ''
  } else {
    alert('할일을 입력하세요.')
    // 빈 문자열 입력 방지. 따로 경고창이 뜸
  }
}

btn.addEventListener('click',addTodo)
```
- 로또 번호 생성기 구현
```html

<script src="
https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js
">
// 자주쓰는 라이브러리 lodash
// const h1Tag = document.querySelector('h1')
const btn = document.querySelector('#btn')
const divTag = document.querySelector('div')

const getLottery = function (event) {
  const numbers = _.range(1,46)
  const sixNumbers = _.sampleSize(numbers,6)

  const ulTag = document.createElement('ul')

  sixNumbers.forEach(number) => {
    const liTag = document.createElement('ul')
    liTag.textContent = number
    ulTag.appendChild(liTag)
  }
  divTag.appendChild(ulTag)
}
btn.addEventListener('click',getLottery)
</script>

```

- 이벤트 기본동작 취소
  - .preventDefault()
    - form 제출이벤트 취소 - 페이지 새로고침 막음
    - copy 이벤트 취소
