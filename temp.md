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

