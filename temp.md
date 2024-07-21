Truthy Falsy
- 참이나 거짓을 의미하지 않는 값도 조건문 내에서 참이나 거짓으로 평가하는 특징
- Falsy: undefined , null ,0, -0, NaN , "" , 0n
- Truthy 는 나머지
- 변수값이 Falsy한 값일 때 그냥 if (!person) {} 같이 작성하면 됨

단락평가
- && , || 에서 첫번째 값으로 표현식을 끝내는 것. 두번째 값, 함수에는 접근도 안하는 것
- 위에 if 안하고 그냥 console.log(person && person.name) 같이 써도 됨
- const name = person && person.name
  console.log(name || "person의 값이 없음");
  첫 줄에는 person 객체값이 있을 경우 person.name이 저장되고 두번째 줄에서 name이 출력
  없을 경우 undefined 저장되고 두번째 줄에서 person의 값이 없음 출력

구조분해할당
- 개수 맞춰서 들어가기. 선언하는 변수개수 만큼만 가져옴. 없을 때 기본값 설정도 가능
- 객체의 키값들 = 객체 이런식으로 value들을 변수에 저장할 수있음
  let {age: myAge,hobby} = person 이런 식으로 다른 이름의 변수에도 저장 가능
- 함수의 매개변수 받는 방법
    const func = ({name,age,hobby,extra}) => {
        console.log({name,age,hobby,extra});
    }

    func(person);

Spread 연산자, Rest 매개변수
- 객체나 배열에 저장된 여러개의 값을 개별로 흩뿌려주는 역할
```js
let arr1 = [1,2,3];
let arr2 = [4,...arr1,5,6];

let obj1 = {
    a:1,
    b:2,
};

let obj2 = {
    ...obj1,
    c:3,
    d:4,
};

function funcA(p1, p2,p3) {
    console.log(p1,p2,p3);

}

funcA(...arr1)
```
- Rest는 나머지 매개변수. 배열형태로. Spread와 반대. Rest 매개변수는 마지막에 오도록 설정해야됨
``` JavaScript
function funcB(one,...rest) {
    console.log(rest);
}

funcB(...arr1);
```

원시타입, 객체타입
- 값이 저장되거나 복사되는 과정이 다르기 때문에 분리. 값 자체 vs 참조값
- 메모리에 원본 데이터를 생성하고 변수가 해당 값을 가리키게 주소 저장. 메모리에 저장된 데이터는 불변임. 삭제되지않음
- 객체타입은 데이터 저장소의 위치인 참조값을 가짐
  프로퍼티 복사를 위해서는 {...o1}; 같이 진행.
  객체 간 비교는 기본적으로 참조값을 기준으로 이루어짐
  내부 프로퍼티 비교는 JSON.stringify(o1) === JSON.stringify(o2) 같이 내장함수 이용

순회
- for of 는 배열
- for in 은 객체
- Object.keys(person), Object.values(person) 키값, 프로퍼티값 배열로 반환

배열 메서드
- push, pop, shift(맨앞 pop),unshift(맨 앞 추가)
- .slice(2,5) 잘라내서 배열 반환 slice(-3)은 뒤에서부터 3개

순회 메서드
- forEach
    arr1.forEach(function(item,idx,arr) {
        console.log(idx,item*2);
    });
    arr1.forEach((item,idx,arr) => {
        console.log(idx,item*2);
    });
    같이 각각의 요소에 특정 동작 수행

- .includes(10) 안에 10 있는지없는지. 참거짓 반환
- .indexOf(2) 특정 요소의 인덱스 찾아서 반환. 없으면 -1
- .findindex((item) => {
    if (item === 2) return true;
})
    모든 요소를 순회하면서 콜백함수를 만족하는 특정요소의 인덱스를 반환하는 메서드.객체타입용.없으면 -1
        .findindex((item) => item%2 !== 0 );
- find((item) => item.name == "이정환"); 객체 반환

배열 변형 메서드
- .filter((item)=> {
    <!-- if (item.name === "이정환" return true) -->
    item.name === "이정환"
}); 
    조건 만족하는 요소들의 배열 반환

- .map((item,idx,arr) => {
    return item*2
})
    .map((item)=>item.name);
배열의 모든 요소를 순회하면서 콜백함수를 실행하고 . 그결과값들을 모아서 새로운 배열로 반환

- .sort() 사전순으로 정렬하는 메서드. 숫자의 대소관계로 비교하려할때는
    .sort((a,b) => {
        if (a>b) {
            return 1;

    } else if (a<b) {
        return -1;
    } else {
        return 0;
    }
    });

-.toSorted()
    새로운 배열 반환

- .join()
    배열의 모든 요소들 합쳐서 문자열로 출력. 구분자는 인수로 넣으셈

데이트 객체
```js
let date1 = new Date(); //생성자. 지금 시간으로
let date2 = new Date("1997-01-07/10:10:10");
```
- 타임 스탬프: 특정 시간으로부터 몇 ms 가 지났는지
    let ts1 = date1.getTime();

    let date4 = new Date(ts1);

- 시간 요소들을 추출하는 방법
let year = date1.getFullYear();
let month = date1.getMonth()+1;
let date = date1.getDate();

- 시간 수정하기
date1.setFullYear(2023);

- 시간을 여러 포맷으루 출력
    .toDateString()
    .toLocaleDateString()

동기와 비동기
- 동기: 작업을 하나에 하나씩. 멀티쓰레드로 문제해결가능, but js는 싱글쓰레드
- 비동기: 동시에. 각각의 task에 callback함수 붙여줘서 끝나면 수행. setTimeout(() => {
    console.log(2);
},3000)
    비동기적으로. 3초뒤에 실행. 싱글스레드지만 비동기작업들을 할 . 수있는 이유는 비동기 작업들은 Web APIs에서 실행됨. 비동기함수의 경우 webAPis에 타이머랑 콜백함수 넘겨주고 타이머 끝나면 콜백함수 리턴

콜백함수
```js
function add(a,b,callback) {
    steTimeout(() => {
        const sum = a*b;
        callback(sum);

    },3000);
}
add(1,2,(value) => {
    console.log(value);
})

```
- 함수 외부에서 사용하고 싶을 때 콜백함수 같이 넣어줘서 출력

```js
function orderFood(callback) {
    setTimeout(() => {
        const food = "떡볶이";
        callback(food);

    },3000);
}

function cooldownFood(food,callback) {
    setTimeout(() => {
        const cooldownedFood = `식은 ${food}`;
        callback(cooldownedFood);
    },2000);
}

orderFood((food) => {
    console.log(food);
    cooldownFood(food, (cooldownedFood) => {
        console.log(cooldownedFood);
});
    });
```

Promise
- 비동기작업를 효율적으로 도와주는 내장객체
Pending(로딩) Fullfilled(resolve) Rejected(reject)

```js
const promise = new Promise((resolve,reject) => {
    // 비동기 작업 실행하는 함수 executor
    setTimeout(() => {
        console.log("안녕");
        resolve("안녕");
        // promise 객체 상태, 결과값 변경
    },2000
    );
});

// console.log(promise);
setTimeout(() => {
    console.log(promise);
},3000);
// 객체출력, 내부함수 출력.

promise.then(()=> {});
// 성공 시 결과값을 인수로 콜백함수 실행, 실패시 실행되지않음
promise.catch(()=>{});
// 실패 시

promise.then(()=>{}).catch(()=>{});
// then이나 catch도 똑같이 promise 객체를 반환하기때문에 이렇게 작성가능
// then 내부에서 return 시 반환값이 결과값으로 됨. 마지막에 catch 처리
```

async/await
- 어떤 함수를 비동기 함수로 만들어주는 키워드
- 함수가 프로미스를 반환하도록 해주는 기워드
- await: async 함수 내부에서만 사용이 가능한 키워드
    비동기 함수가 다 처리되기를 기다리는 역할
```js
async function getDate() {
    return {
        name:"이정훈",
        id:"winterlood"
    };
}
// 함수를 반환값을 결과값으로 가지는 promise 객체로 바꿔줌.

// function printData() {
//     getdata().then((result) => {
//         console.log(result);
//     });
// }
// printData();

async function printData() {
    const data = await getdata();
    console.log(data);
}
printData();
```

Node.js
- javaScript 실행환경
- npm: node package manager
- 패키지: Node.js에서 사용하는 프로그램의 단위
    npm init 
    node 파일 : 파일 실행
    package.json에 scripts에 매크로같은거 작성가능

- 모듈 시스템
    모듈: 기능별로 파일 분리해서 개발
    CJS: module.exports = {내보낼 값}, 키랑     변수값 넣어줌. 같은 이름일 경우 하나만 써도 됨. 
    const {add, sub} = require("./math"); 로 모듈데이터 가져옴. 객체 분해할당

    ESM: package.json에 "type":"module" 추가
    CJS랑 같이 쓸 수는 없음. 
        export { add , sub};
        import {add , sub} from "./math.js";
    
        확장자까지 명시
        함수 선언문 앞에다 export 적어도 ㄱㅊ
        export default 앞에다 붙이면 대표하는 값
        불러오는 곳에서 {} 안붙이고 가져오기 가능. 이름도 바꿔도 ㄱㅊ

라이브러리
- npmjs.com 에서 필요한 라이브러리 설치 후 사용
- import randomColor from "randomColor"
- npm i or npm install: package.json 기반으로 다시 다 설치해줌. node_modules는 gitignore로 처리함.

React.js
- 컴포넌트 기반(코드 수정 용이),
 화면 업데이트 구현 용이(선언형 프로그래밍_ 과정 생략, 목적 간결, 각각의 component에는 state 존재, state상태에 따라 랜더링 다르게), 
 빠름(Critical Rendering Path, Dom은 HTML을 객체의 객체 버전. 화면의 업데이트는 js가 DOM을 수정해서 발생.layout,painting은 오래걸림.업데이트 다 처리후 Dom 수정_virtualDom(buffer역할)).

- Node.js 패키지 생성, React 라이브러리 설치, 기타 도구 설치 및 설정(vite)
    - npm create vite@latest
    - 파일/폴더열기 ㅁㅊ
    - npm install로 라이브러리들 설치
    - public: 이미지파일, 폰트, 동영상들 저장용
      src(source): 코드 저장용,assets에도 정적파일 저장가능
      eslintrc.cjs:코드스타일 통일용
      index.html: 출력용 기본틀
    - scripts
        npm run dev


- 구동원리
    - 리액트 웹서버 내장
    - 포트번호
    - index.html -> main.jsx -> App.jsx(컴포넌트)

실습준비
- assets/react.svg , public/vite.svg 삭제. usestate 삭제, app함수가 리턴하고 있는 div 다 삭제. app.css 다 삭제. main.jsx 에 React.StrictMode 삭제. .eslintrc.cjs 에 rules 에 'no-unused-vars':"off" 랑 "react/prop-types":"off" 추가

React 컴포넌트
- 컴포넌트:html 태그들을 반환하는 함수. 화살표 함수로도 가능. 클래스로도 가능하긴한데 귀찮다.
  반드시 첫글자는 대문자. 컴포넌트는 main.jsx에 render해야됨. <Header/> 를 부모컴포넌트 안에 넣어줌. 다른 컴포넌트 리턴에 들어가는 컴포넌트는 자식컴포넌트
  모든 컴포넌트들의 최상위 조상, App은 루트컴포넌트. 보통 관례상 App을 루트로 놓음.
- src/components 에 jsx인 컴포넌트 파일들을 만들고 안에 함수를 작성한 다음 export default 함수명을 추가. App.jsx에서 컴포넌트 불러와서 렌더링

jsx
- js와 html 혼용. return(<h2>{number}</h2>) 같이 사용. 안에서 연산도 가능
- 중괄호 내부에는 자바스크립트 표현식만 넣을 수 있다.
- 숫자, 문자열, 배열값만 렌더링 된다. true, null, undefined 같은 값은 랜더링 안됨. 객체넣으면 에러남.
- 모든 태그는 닫혀있어야된다
- 최상위 태그는 반드시 하나여야만 한다.넣을만한게 없으면 빈 태그만 해줘도 됨. 그럼 리턴될때 최상위 태그 없는 걸로 랜더링
- 상태별로 리턴 다르게 하는거는 조건문으로 하거나 {}내에서 삼항연산자로 하거나.
- 스타일은 style={{backgroundColor: "red"}} 을 태그에 넣음. 카멜케이스로 작성. 
    - css파일로 하려면 파일명.css로 하고 import "./파일명.css"; className="클래스이름" 태그에 넣기

props
- 컴포넌트에 값전달하기.
ex)네이버: searchBar, Button(반복) 컴포넌트.
- <Button text={"카페"} img={"cafe.png"} /> 이렇게 값 전달
```javascript
const Button = (props) => {
    concole.log(props);
    return (<button>{props.text}</button>);
};
Button.defaultProps = {
    color:"black",
};
// 이렇게 오류도 방지
// props에 {text, color} 같이 객체분해할당으로 받아도 ㄱㅊ.
// 안에 컴포넌트나 html을 넣으면 children에 들어감
```

Event Handling
- 이벤트 발생시 처리.
- buttin 태그에 onClick={()=>{console.log(text);}} 을 넣거나 함수를 만들어서 함수만 넣거나.익명 or 기명
- 함수의 이름만 넣기. onMouseEnter 에도 똑같이
- 이벤트 객체가 매개변수로 들어감. 합성이벤트: 모든 웹브라우저의 이벤트 객체를 하나로 통합한거_crossBrowsing이슈 해결.

State
- 현재 가지고 있는 형태나 모양을 정의, 변화할 수 있는 동적인 값
- 모든 컴포넌트가 가지고 있음
- 상태변화(리랜더링)에 따라 랜더링 결과 달라짐
- 하나의 컴포넌트에 여러 스테이트 가능
```js
import {useState} from "react";
function App() {
    // const state = useState(0);
    const {state,setState} = useState(0);
    // 스테이트 값(초기값 설정 가능), 함수(상태변화함수) 

    return (
    <>
        <h1>{state}
        <h1/>
        <button onClink={()=>{
            setState(state+1);
            }}
            >
            +
            <button/>
    </>
);
}
{/* 누르면 App함수 다시 호출 */}
```
- 변수안만들고 state 만드는 이유: 리랜더링 시킬려고. 

State를 Props로 전달하기
- 자식컨퍼넌트에게 주는 props가 바뀌게 되면 리랜더링 발생
- state값 변경시, props값 변경시, 부모컴포넌트 리랜더링시 리랜더링_이것때문에 컴포넌트 안에 상태 넣어줌
-

State로 사용자 상태 관리하기
```javascript
const Register = () => {
    const {name,setName} = useState("이름");
    const {birth,setBirth} = useState("");
    const {country,setCountry} = useState("");
    const {bio,setBio} = useState("");
    const onChangeName = (e) => {
        console.log(e);
        setName(e.target.value);
    }
    const onChangeBirth = (e) => {
        setBirth(e.target.value);
    }
    const onChangeCountry = (e) => {
        setCountry(e.target.value);
    }
    const onChangeBio = (e) => {
        setBio(e.target.value);
    }
    return (
        <div>
            <div>
            <input value={name} onChange={onChangName} placeholder={"이름"} />
            </div>
            {/* 초기값 설정 */}
            <div>
            <input value={birth} onChange={onChangBirth} type="date" />
            </div>
            <div>
                <select value={country} onChange={onChangeCountry}>
                    <option></option>
                    <option value="kr">한국</option>
                    <option value="us">미국</option>
                    <option value="uk">영국</option>
            </div>
            <div>
                <textarea value={bio} onChange={onChangeBio}></textarea>
            </div>
        </div>
    );
};

export default Register;
```

```javascript
const {input, setInput} = useState({
    name:"",
    birth:"",
    country: "",
    bio: "",
});

// const onChangeName = (e) => {
//     setInput({
//         ...input,
//         name : e.target.value,
//     });
// };
const OnChange = (e) => {
    setInput({
        ...input,
        [e.target.value]:e.target.value,
        // 키 자리에 대괄호를 열고 변수를 넣으면 이걸 키로 넣음. input의 name을 키로 설정해서 value 넣음
    });
};
...

// input.country 같이 접근. name="name" 도 추가.
```

useRef
- 새로운 Reference 객체를 생성.
- 값이 변경해도 리랜더링 유발하지 않음
- 특정 돔요소 접근 가능

```javascript
import {useState, useRef} from "react";

const inputRef = useRef();
// inputRef 사용 이유: 리랜더링되면서 리셋됨.
// 컴포넌트 외부에 선언하게되면 해당 컴포넌트 여러번 호출 시 변수 공유하게됨

const onSubmit = () => {
    if (input.name ==="") {
        inputRef.current.focus();
    }
};

ref = {inputRef}



// current에 값 저장하는 객체
// 변경되도 해당 컴포넌트 리랜더링 x.
// 화면에 표시되지않는 내부적인 값 측정 시. 카운트 횟수같이
```
reactHooks
- 함수 컴포넌트에서도 클래스 컴포넌트 기능 다 쓰기
- useRef 같은 것들도 React Hooks. 앞에 use가 붙음
- 함수컴포넌트내에서만 호출가능, 조건문,반복문내에서는 호출 불가, 나만의 훅 제작가능
- 자주 쓰는 로직들을 커스텀 훅으로 만들기. 따로 빼서 리턴만 잘해주기, 앞에 use 붙이기
-  src/hooks/훅이름.jsx

라이프사이클
- mount(처음 랜더링된 순간), update(마운트 이후에 다시 리랜더링 되는 순간), unMount(랜더링에서 제외되는 순간)
- 라이프 사이클 제어_useEffect

useEffect
- 사이드이펙트 제어.
- 라이프 사이클에 맞춰 출력
- useEffect(()=>{
    console.log(`count: ${count}`);
},[count]);
    count 상태가 변경될때마다 콜백함수 실행. 배열에 의존_의존성 배열

- console.log를 하나하나 안하는 이유: setCount는 비동기로 실행하기때문. 바로바로 반영 x

const isMount = useRef(false);
- mount: useEffect(()=>{console.log("mount")},[]);
- update: useEffect(()=>{if (!isMount.current) {isMount.current = true; return;} console.log("update")});
- unmount: 컴포넌트안에  useEffect(()=>{return () => {console.log("unMount")};},[]);
 클린업, 정리함수. useEffect가 끝날 때 실행됨.

리엑터 디벨로퍼 툴스.


useReducer
- 컴포넌트 내부에 새로운 state를 생성하는 리액트 훅
- 모든 useState를 대체가능. 
- 상태관리 코드를 컴포넌트 외부로 분리할 수 있음
- 외부에 Reducer 함수 작성
function reducer(state,action) {
    if (action.type === "INCREASE") {
        return state + action.data;
    }
}
- 상태를 실제로 변환시키는 변환기 역할
const {state, dispatch} = useReducer(reducer,0);
- dispatch 상태변화가 있어야 한다는 사실을 알리는 함수
const onClickPlus = () =>{
    dispatch({
        type: "INCREASE",
        data:1
        <!-- 상대가 어떻게 변하길 원하는지_액션객체 -->
    });
}
- action의 타입이 많아지면 switch로 작성
- 근데 state가 여러개면 어떻게?

최적화
- useMemo: 메모이제이션으로 불필요한 연산 최소화
const {totalCount, doneCount, notDonCount} = useMemo (()=> {실행코드},[todos]); 
- useEffect에서 depth가 바뀌면 콜백 다시 실행하는 것처럼. 콜백함수가 반환하는 값 그대로 반환.
- 연산 한번만 수행

React.memo
- 컴포넌트를 인수로 받아 최적화된 컴포넌트로 만들어 반환
const MemorizedComponent = memo(Component);
- 부모가 리랜더링 되더라도 리랜더링x(props가 바뀌지 않으면) memo로 최적화됨
import { memo} from "react"
...
<!-- const memorizedHeader = memo(Header); -->
<!-- export default memorizedHeader; -->
export default memo(Header);
- app컴포넌트가 리랜더링되면 함수타입은 객체. 함수들이 계속 다시 생성되면서 주소값이 달라져 다른 값이라고 판단. 모두 리랜더링
- memo는 얕은 비교 === 라 달라졌다고 판단. (객체타입 props를 가졌을경우)
export default memo(TodoItem, (prevProps,nextProps) => {
    if (prevProps.id !== nextProps.id) return false;
    if (prevProps.isDone !== nextProps.isDone) return false;
    if (prevProps.content !== nextProps.content) return false;
    if (prevProps.date !== nextProps.date) return false;

    return true;
    <!-- 리랜더링 하지 마라 -->

});
- 고차 컴포넌트

useCallback
const onDelete = useCallback(useReducer때 작성한 코드);

- 최적화는 언제 어떻게? 일단 기능 다 완성 후 최적화. 꼭 필요해보이는 곳만.

Context
- 컴포넌트간의 데이터를 전달하는 다른 방법
- 기존의 부모 -> 자식 데이터 전달. 프롭스드릴링
- 데이터 보관소 (객체). 함수,객체 저장. 여러개 생성해서 컴포넌트 별로 데이터 제공 가능
import {createContext} from "react";
export const TodoContext = createContext();
- 보통 컴포넌트 외부에 작성,Provider
<TodoContext.Provider value={{todos,onCreate}}>
    내부에 자식들 TodoContext 바로 접근 가능
</TodoContext.Provider>


import {useContext} from "react";
import {TodoContext} from "../App";

const {onCreate} = useContext(TodoContext);

- 근데 최적화 풀림. 자식쪽에서 값 변경하면 부모쪽 리랜더링 발생. 객체 자체가 다시 생성
- todoContext를 두개로 분리. todoStateContext_변경될 수 있는 값 todoDispatchContext_변경되지않는값
<todoStateContext.Provider value={{todos}}>
    <todoDispatchContext.Provider value={{onCreate}}>
    이 valuesms useMemo로
    내부에 자식들 TodoContext 바로 접근 가능
</todoDispatchContext.Provider>
</todoStateContext.Provider>


카운터앱
- 할거하고 app.css, index.css 내부 삭제
- section 태그로 묶어주면 컴포넌트들마다 내부여백, 백그라운드 설정
- 태그에 className="App"이라고 적어주면 App.css에 .App에서 css설정가능.
전체 페이지에 padding, 각 section에 padding, margin-bottom.
margin 0 auto; width:400px;
- app 컴포넌트(부모)에 useState 작성. 자식간 데이터전달 불가능.
- 그리고 각 컴포넌트에 변수, {변수, 함수}를 전달. 함수는 이벤트 핸들러를 따로 만들어서 전달. onClick={화살표 함수} 로 사용
- 단방향 데이터 흐름

투두리스트
- 이것만 봐도 이쁘네
```javascript
// App.css
.App {
    display: flex;
    // 자식요소들이 가로로 붙어서 출력
    flex-direction: column;
    // 세로로 출력
    gap:10px;
    // 요소들간 간격, flex일때만 사용가능
    width: 500px;
    margin:0 auto;
    // 가운데 정렬
}

// Header.jsx
import './Header.css';
const Header = () => {
    return (
        <div className="Header">
            <h1>(new Date().toDateString())</h1>
        </div>
    );
};

export default Header;

// Header.css
.Header > h1 {
    color: rgb(37,147,255);
}

// Editor.jsx

import {useState,useRef} from "react";
const Editor = (onCreate) => {
    const [content, setContent] = useState("");
    const contentRef = useRef();
    const OnChangeContent = (e) => {
        setContent(e.target.value);
    };

    const onSubmit = () => {
        if (content === "") {
            contentRef.current.focus();
            // 반짝
            return;
        }
        onCreate(content);
        setContent("");
        // 초기화
    };

    const onKeyDown = (e) => {
        if (e.keyCode === 13) {
            onSubmit();
        }
    };
    // 사용자가 어떤 키를 눌렀는지
    return (
        <div className="Editor">
            <input value={content}
            onKeyDown={onKeyDown}
            ref = {contentRef}
            onChange={onChangeContent}
            placeholder="새로운 Todo..." />
            <button onClick={onSubmit}>추가</button>
        </div>
    );
};

export default Editor;

//Editor.css
.Editor {
    display: flex;
    gap:10px;
}

.Editor input {
    flex: 1;
    // 부모요소의 범위를 벗어나지 않는 선에서 최대한 늘어남
    padding:15px;
    border:1px solid #rgb(220,220,220);
    border-radius:5px;
}

.Editor button {
    cursor: pointer;
    // 마우스 커서 올리면 포인터로 바뀜
    width:80px;
    border: none;
    background-color: #rgb(37,147,255);
    color: #white;
    border-radius:5px;

}

}

// List.jsx
import "./List.css";
import TodoItem from "./TodoItem";
import {useState} from "react";
const List = ({todos, onUpdate,onDelete}) => {
    const [search, setSearch] = useState("");

    const OnChangeSearch = (e) => {
        setSearch(e.target.value);
    }

    const getFilteredData = () => {
        if (search ==="") {
            return todos;
        }
        return todos.filter((todo)=>todo.content.toLowerCase().includes(search.toLowerCase()));
    }

    const filteredTodos = getFilteredData();
    return (
        <div>
            <h4>Todo List</h4>
            <input value = {search} onChange={onChangeSearch} placeholder="검색어를 입력하세요"/>
            <div className="todos_wrapper">
                {filteredTodos.map((todo)=>{
                    {/* return <div>{todo.content}</div>; */}
                    return <TodoItem key={todo.id} {...todo} onUpdate={onUpdate} onDelete={onDelete} />;
                    {/* key 필요 */}
                    {/* 컴포넌트로도 리턴가능, props로 전달도 가능 */}
                })}
            </div>
        </div>
    );
};

export default List;

//List.css
.List {
    display:flex;
    flex-direction:column;
    gap:20px;
}
.List > input {
    width: 100%;
    border:none;
    border-bottom: 1px solid #rgb(220,220,220);
    // 밑에 테두리만
    padding:15px 0px; // 위 아래만

}

.List > input:focus {
    // focus되었을때
    outline: none;
    border-bottom: 1px solid #rgb(3,147,255);
}

.List .todos_wrapper {
    display:flex;
    flex-direction:column;
    gap:20px;
}

// TodoItem.jsx
import './TodoItem.css'
const TodoItem = ({id, isDone, content, date, onUpdate,onDelete}) => {
    
    const onChangeCheckbox = () => {
        onUpdate(id);
    };

    const onClickDeleteButton = () => {
        onDelete(id);
    };

    
    return <div className="TodoItem"> 
        <input onChange={onChangeCheckbox} checked={isDone} type="checkbox" />
        <div className="content">{content}</div>
        <div className="data">{new Date(date).toLocalDateString()}</div>
        <button onClick={onClickDeleteButton}>삭제</button>
    </div>;
};

export default TodoItem;

// TodoItem.css
.TodoItem {
    display:flex;
    alignItems:center;
    // 가운데 정렬
    gap:20px;
    padding:bottom;
    border: 1px solid #rgb(240,240,240);
}
.TodoItem input {
    width:20px;
}

.TodoItem content {
    flex:1;
}

.TodoItem .date {
    font-size:14px;
    color:gray;
}

.TodoItem button {
    cursor:pointer;
    color:gray;
    font-size:14px;
    border: none;
    border-radius: 5px;
    padding: 5px;
}

//App.jsx

import { useState, useRef} from 'react';
const mockData = [
        {
            id:0,
            isDone:false,
            content: "공부하기",
            data : new Date.getTime(),
        },
        {
            id:0,
            isDone:false,
            content: "공부하기",
            data : new Date.getTime(),
        },
    ]

function App() {
    
    const [todos,setTodos] = useState(mockData)
    const idRef = useRef(3);
    const onCreate = (content) => {
        const newTodo = {
            id:idRef.current++,,
            isDone:false,
            content: content,
            data: new Date().getTime()
        }

        // todos.push(newTodo);;
        setTodos([newTodo,...todos])
    };
    const onUpdate = (targetId) => {
        setTodos(todos.map((todo) => todo.id === target.id ? {...todo, isDone:!todo.isDone} : todo));
    };

    const onDelete = (targetId) => {
        setTodos(todos.filter((todos) => todos.id !== targetId));
    };


    return (
        <div className="App">
            <Header />
            <Editor onCreate={onCreate}/>
            <List todos ={todos} onUpdate={onUpdate} onDelete={onDelete}/>
        </div>
    );
};
```
App

MPA(매번 전체 랜더링, 서버부하) , serverSide.
->SPA. index.html 하나 존재. 자스 파일들 하나의 파일로 전달(번들링. 번들파일_리액트앱_비트가 담당). 브라우저에서 랜더링 처리_클라이언트 사이드 랜더링. 리액트앱으로 자체적으로 화면교체.

리액트 라우터: 대표격 라이브러리

동적 경로: 동적인 데이터를 포함하고 있는 경로
- URL Parameter(/뒤에 아이템의 id를 명시,잘 변경되지 않는 값) , Query String(?뒤에 변수명과 값 명시, 자주 변경되는 값)

폰트는 public 이미지는 assets. vites에서 이미지 최적화를 해줘서

빌드 후 프리뷰 했을 때 차이가 큼.데이터uri로 저장된 애들은 캐싱되서 한번 가져오면 다음엔 그냥 불러옴. 불러올 데이터가 너무 많으면 public이 나을 수도.

모든 페이지에서 사용. useReducer사용. props나 context 둘다 부모에서 자식 방향으로만. 그리고 context 사용. 
useContext로 꺼내서 사용
복잡한 로직 함수. 매개변수만으로도 필요한 데이터 제공받는다면 컴포넌트 외부에 선언해도 ㄱㅊ.

웹 스토리지: 새로고침 시에도 유지되게. 웹브라우저 내부 db, 자바스크립트 내장함수만으로도 가능.
    setItem(key, value);
    getItem(key);
    세션 스토리지(브라우저 탭 끄면 끝), 로컬 스토리지(사이트 주소별로. 직접삭제하기 전까지 보관).

