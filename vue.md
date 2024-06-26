## Fronted Development
### client-side frameworks
- 클라이언트 측에서 UI와 상호작용을 개발하기위해 사용되는 JavaScript 기반 프레임워크
  - 웹에서 하는 일이 많아짐_ 다루는 데이터가 많아짐
  - 어플리케이션의 상태가 변경될 때마다 일치하도록 UI를 업데이트 해야함
  - 하나하나 연결하면 너무 빡셈

- SPA: 단일 페이지로 구성된 어플리케이션
  - 하나의 html 파일로 시작하여 사용자가 상호작용할 때마다 페이지 전체를 새로 로드하지않고 화면의 필요한 부분만 동적으로 갱신.
  - 대부분 JavaScript 프레임워크를 사용하여 클라이언트 측에서 UI와 렌더링을 관리
  - CSR 방식 사용
- CSR: 클라이언트에서 화면을 렌더링하는 방식  
  - 최초에만 페이지를 받고 javascript를 사용해서 계속 DOM 업데이트, 페이지를 렌더링
  - 서버는 더이상 HTML을 제공하지 않고 요청에 필요한 데이터만 응답
  - 페이지 갱신 시 새로고침이 없는 이유
  - 빠른 페이지 전환, 사용자 경험, 프론드 백엔드 분리
  - 느린 초기 로드 속도. SEO(검색엔진 최적화) 문제_html에 아직 콘텐츠가 모두 존재하지 않기때문
- SPA vs MPA(여려개의 html파일이 서버로부터 각각 로드. 이동 시 새로운 hmtl 로드)
- CSR vs SSR(서버에서 화면을 렌더링하는 방식. 서버에서 모든 데이터 넣은 html 완성후 클라이언트에 전달)

# VUE
- 사용자 인터페이스를 구축하기 위한 JavaScript 프레임워크
- VUE 2 문서에 접속하지 않도록 주의
- 쉬운 학습곡선, 확정성과 생태계, 유연성 및 성능
- 핵심기능
  - 선언적 렌더링 {}
  - 반응성
- CDN방식
  - CDN 작성 후
```html
<script>
  const { createApp , ref} = Vue
  // 전역 Vue 객체 불러오기
  const app = createApp({
    setup() {
      const message = ref('Hello vue!')
      // ref() : 반응형 상태(데이터)를 선언하는 함수.
      //  반응형을 가지는 참조변수를 만드는 것
      // ref로 선언된 변수의 값이 변경되면 해당 값을 사용하는 템플릿에서 자동으로 업데이트
      console.log(message) //ref 객체
      console.log(message.value) // Hello vue!
      return {
        message
      }
      // 반환필요
      // 함수내에서 값 접근시 .value 필수
    }
  })
  // 새 Application instance 생성
 
  app.mount('#app')
  // HTML요소에 Vue 애플리케이션 인스턴스를 연결. 각 앱 인스턴스에 대해 mount()는 한번만 호출 가능
</script>
```
- v_on directive를 사용하여 DOM 이벤트를 수신할 수 있음
- NPM방식

- ref 객체가 필요한 이유
  - 객체 데이터 타입으로 사용하는 이유는  의존성 추적 기반의 반응형 시스템_참조 자료형의 객체 타입으로 구현

# Syntzx
## template syntax
- 선언적으로 바인딩(vue instance와 Dom을 연결)할 수 있는 템플릿 구문 사용
- text interpolation {{}}
  - 데이터 바인딩의 가장 기본적인 형태. 실시간 업데이트
- Raw HTML: 실제 HTML을 출력하려면 v-html을 사용해야함
  - 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문
- Attribute Bindings: 콧수염 구문은 HTML속성내에서 사용할 수 없기 때문에 v-bind를 사용. 


## computed Properties
- 계산된 속성 을 정의하는 함수. 미리 계산된 속성을 사용하여 반복연산을 줄임
- 반응형 데이터를 포함하는 복잡한 로직의 경우 computed를 활용하여 미리 값을 계산하여 계산된 값을 사용
- 반환되는 값은 computed ref, 일반 ref랑 비슷하게 사용
- 의존된 반응형데이터를 자동으로 추적
- 의존하는 데이터가 변경할 때만 재평가.
- computed vs method
  - 의존된 반응형 데이터를 기반으로 캐시_의존된 반응형 데이터가 변경될때만 <-> 랜더링 발생할 때마다 항상 함수 실행(항상 동일한 결과)
  - 캐시: 데이터나 결과를 일시적으로 저장해두는 임시 저장소
  - 이후 같은 데이터나 결과를 다시 계산하지않고 빠르게 접근할 수 있도록 함

## Conditional Rendering
- v-if,v-else,v-else-if
- <div v-if="name === 'Alice'">앨리스임</div>
- <template 에 넣기> : 렌더링은 안됨
  - v-if vs v-show(일단 그림. 대신 히든으로 가림.온오프의 개념)
  - 처음에 비용 적음, 토글비용 높음 vs 초기조건 관계없이 항상 렌더링. 초기 렌더링 비용이 높음\

## List Rendering
- v-for: value, (value, key), (value,key,index) 순서.
  - 인덱스(객체에서는 key)에 대한 별칭 지정 가능
  - key랑 같이쓰자. 순서보장을 위해
  - <div v-for="item in items" :key="item.id"> </div>
  - key는 number or string
  - v-for랑 v-if 같이 쓰면 v-if가 먼저 실행됨
  <!-- 요까정 -->
    - computed활용: 먼저 배열을 새로 만듦
    - 
    - v-for, <template>요소 활용

- watch: 하나 이상의 반응형 데이터를 감시하고 감시하는 데이터가 변경되면 콜백함수 호출.(작업을 수행,axios에서 자주 사용) computed랑 비슷(의존하는 데이터 속성의 계산된 값,중복계산 방지).
  - 둘 다 원본 데이터를 직접 변경하지않음

# single-File components
- component: 재사용 가능한 코드블록
  - UI를 독립적이고 재사용가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
  - 애플리케이션은 중첩된 Component의 트리형태로 구성됨
- single-file component(SFC): 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식(.vue파일)
  - template, script, style 블록으로 분할.
  - v-base-3-setup 자동완성 클릭. scss만 지움
```vue
<template>
  <div>
    <p class="'greeting'"> {{msg}}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('Hello')

</script>

<style scoped>
  .greeting {
    color: aqua;
  }
</style>
<!-- 순서는 상관없음 -->
<!-- template 블록은 1개만. script setup도 하나 -->
<!-- scoped가 지정되면 css는 현재 컴포넌트에만 적용됨 -->
```

## SFC build tool
- Vite: 프론트엔드 개발도구
  - vite 프로젝트 생성
    - npm create vue@latest
    - 다 no
  
- NPM: Node.js의 기본 패키지 관리자(pip 같은 놈)
- node.js: 자바스크립트 기반 serverSide 실행환경
  - 풀스택 개발 가능. 다양한 오픈소스 패키지, 라이브러리 제공
- 모듈: 프로그램을 구성하는 독립적인 코드블록(.js파일)
  - 의존성 문제
- Bundler: 여러 모듈과 파일을 하나 혹은 여러개의 번들로 묶어 최적화
  - 의존성관리, 코드최적화, 리소스관리

- node_modules(venv같은거)
  - 의존성 모듈 저장,관리
  - 라이브러리, 패키지 포함
- package-lock.json
  - requirement같은거
- package.json
  - readme 같은 거
- public 디렉토리
  - 소스코드에서 참조되지 ㅇ낳는, 항상 같은 이름을 갖는 import 할 필요 없는애들
  - root 절대경로로 접근
- src 디렉토리
  - 주요 소스코드를 포함하는 곳
  - assets
    - 프로젝트 내에서 사용되는 자원을 관리
    - 프로젝트 자체에서 참조하는 내부파일을 저장하는 데 사용
    - 컴포넌트가 아닌 곳에서는 public 디렉토리에 위치한 파일을 사용
  - components
    - Vue 컴포넌트들을 작성하는 곳
  - App.vue
    - Vue 앱의 최상위 Root 컴포넌트
    - 다른 하위 컴포넌트들을 포함
    - 애플리케이션 전체의 레이아웃과 공통적인 요소를 정의
  - main.js
    - Vue 인스턴스를 생성하고 애플리케이션을 초기화하는 역할
    - 필요한 라이브러리를 import.하고 전역설정을 수행
  - index.html
    - 앱의 진입점
    - App.vue 가 해당페이지에 마운트됨
    - 외부 리소스를 로드할 수 있음 ex)bootstrap CDN

## Vue Component 활용
  - 라우터
  - 피니아


# Component State Flow
## Passing Props
- 위치상으로 다른 같은 컴포넌트. 여러 개의 위치에서 관리하는 게 아니라 한 곳에서 관리_공통된 부모 컴포넌트에서 관리
- Props: 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는 데 사용되는 속성
  - 부모에서 자식으로만 업데이트 가능. 업데이트 시 자식컴포넌트의 모든 props가 최신값으로 업데이트.
  - 자식은 자신에게 일어난 일 부모에게 emit 
  - One-Way Data Flow: 모든 props는 자식속성과 부모속성 사이에 하향식  단방향 바인딩을 형성
    - 단방향인 이유: 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함
    - 데이터 흐름의 일관성 및 단순화

App.vue
```vue
<template>
  <div>
    <Parent />
  </div>
</template>

<script setup>
  import Parent from '@/components/Parent.vue'


</script>

```

Parent.vue
```vue
<template>
  <div>
    <ParentChild 
      my-msg="message" 
      :dynamic-props="name"
      @some-event="someCallback"
      @my-focus="someCallback2"
      @emit-args="getNumbers"
      @update-name="updateName"
      />
      <!-- 아까는 문자열. 지금은 변수보냄 -->
    <!-- <ParentChild my-msg="message"/> -->
    <ParentItem 
    v-for="item in items"
    :key='item.id'
    :my-prop="item"
    />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import ParentChild from '@/components/ParentChild.vue'
  import ParentItem from '@/components/ParentItem.vue'


  const name = ref('Alice')
  const items = ref([
    {id:1, name: "사과",},
    {id:2, name: "사",},
    {id:3, name: "과",},
  ])
  const someCallback = function(){
    console.log("p c 가 이벤트 수신")
  }
  const someCallback2 = function(){
    console.log("p c 가 이벤트 수신2")
  }

  const getNumbers = function(...args) {
    console.log(args)
  }

  const updateName = function() {
    name.value = 'Bella'
  }
</script>

```

ParentChild.vue
```vue
<template>
  <div>
    
      <!-- props이름 = "props 값" -->
    <p>{{myMsg}}</p>
    <p>{{ dynamicProps }} </p>
    <ParentGrandChild 
    :my-msg="myMsg"
    @update-name = "updateName"/>
    <!-- v-bind를 사용한 동적 props -->
    <button @click= "$emit('someEvent')">b1</button>
    <button @click= "buttonClick">b2</button>
    <button @click= "emitArgs">b3</button>


  </div>
</template>

<script setup>
  import ParentGrandChild from '@/components/ParentGrandChild.vue'

  // defineProps(['myMsg'])
  defineProps({
    myMsg:String,
    dynamicProps:String
  })
  const props = defineProps({ myMsg: String})
  console.log(props.myMsg)
  // 객체 선언 문법 권장
  // props를 선언. 인자의 데이터 타입에 따라 선언 방식이 나뉨
  // html과 js에 맞게 작성
  const emit = defineEmits(['myFocus','myArgs','updateName'])

  const buttonClick = function() {
    emit('myFocus')
  }

  const emitArgs = function() {
    emit('emitArgs',1,2,3)
  }

  const updateName = function () {
    emit('updateName')
  }
</script>

```
- 부모 컴포넌트에서 내려보낸 props를 사용하기 위해서는 자식 컴포넌트에서 명시적인 props 선언이 필요

ParentGrandChild
```vue
<template>
  <div>
    <ParentChild />
    <button @click= "updateName">이름변경</button>

  </div>
</template>

<script setup>
  defineProps({
    myMsg: String
  })

  const emit = defineEmits(['updateName'])

  const updateName = function () {
    emit('updateName')
  }

</script>

```

## Props 세부사항
- Props Name Casing
  - 자식 컴포넌트로 전달시 kebab-case
  - 선언 및 템플릿 참조시 camelCase
- static props , Dynamic props
  - v-bind를 사용하여 동적으로 할당된 props를 사용할 수 있음

## Props 활용

ParentItem.vue
```vue
<template>
  <div>
    <p>{{ myProp.id}}</p>
    <p>{{ myProp.name}}</p>
  </div>
</template>

<script setup>
 defineProps({
  myProp:Object
 })
</script>
  
```

## Component Events
- Emit: 부모가 props 데이터를 변경하도록 요청
  - $emit(): 자식 컴포넌트가 이벤트를 발생시켜 부머컴포넌트로 데이터를 전달하는 역할의 메서드, $는  Vue 인스턴스의 내부변수 가리킴
    - @emit(event,...args)
  - defineEmits() 로 선언

## 이벤트 전달
## Event name casing
  - 자식 먼저 작성. 쓰는 법은 똑같
## 참고
- 객체선언문법: 가독성, 잘못된 유형 시 콘솔에 경고(유효성 검사)

# Router
- Routing: 네트워크에서 경로를 선택하는 프로세스. 다른 페이지 간의 전환과 경로를 관리하는 기술
  - SSR에서 Routing은 서버 측에서 수행
  - CSR에서 Routing은 클라이언츠 측에서 수행
    - 전체 페이지를 다시 로드하지 않음_single page
    - 페이지 변화 감지 불가, 새로고침 시 처음페이지, 첫페이지만 공유가능, 뒤로가기 불가
    - 주소에 따라 여러 컴포넌트를 새로 렌더링하여 마치 여러 페이지를 사용하는 것처럼 보이도록

- Vue Router  
  - 프로젝트 생성 시 Router 추가에 Yes
  - App.vue 코드 변화, router 폴더 신규 생성, views 폴더 신규 생성
    - RouterLink: 페이지를 다시 로드하지 않고 URL을 변경하여 URL 생성 및 관련 로직을 처리,a태그로 랜더링
    - RouterView: RouterLink URL에 해당하는 컴포넌트를 표시. 원하는 곳에 배치 가능

  - router/index.js:url과 컴포넌트를 매핑
  - views: components 폴더와 비슷. RouterView에 실질적으로 랜더링하는 애들

## Basic Routing
- index.js에 라우터 관련 설정 작성. 주소,이름,컴포넌트
- RouterLink의 to 속성으로 index.js에서 정의한 주소값 사용
- Named Routes: 경로에 이름을 지정하는 라우팅
  - :to= "{ name: ''}" 형태로 작성

- Dynamic Router Matching: URL일부를 변수로 사용하여 경로를 동적으로 매칭
  - 매개변수는 콜론 ":" 표기
  - path: '/user/:id'
  - params:{'id':userId} _App.vue
  - 라우트의 매개변수는 컴포넌트에서 {{$route.params.id}} 같이 참조 가능
    - 위랑 아래랑 동일
    - import { useRoute } from 'vue-router'
    - const route = useRoute()
    - const userId = ref(route.params.id) 같이 반응형 변수에 할당 후 템플릿에서 출력. 

- Nested Routes: 중첩된 라우팅
  - 페이지의 일부분 변경
  - children 옵션. index.js에 작성. 앞쪽에 슬래쉬 안붙임
  - 기본 페이지 설정하던가 안하던가 상관 s. 하면 name 없애고 하위 경로 하나 더.
  - 중첩 <-> 부모 자식관계

# Stata Management
- Vue 컴포넌트는 이미 반응형 상태를 관리하고 있음, 상태 === 데이터
- 컴포넌트 구조의 단순화
  - 상태: 앱 구동에 필요한 기본 데이터
  - 뷰: 상태를 선언적으로 매핑하여 시각화
  - 기능: 사용자 입력에 대해 반응적으로 상태 변경

- 상태관리의 단순성이 무너지는 시점
  - 여러 컴포넌트가 상태를 공유할 때
    - 여러 뷰가 동일한 상태에 종속:계층구조가 깊어질 경우 비효율적, 관리가 어려워짐
    - 서로 다른 뷰의 기능이 동일한 상태를 변경: 발신된 이벤트를 통해 여러 복사본을 변경 및 동기화 하는 것. 관리의 패턴이 깨지기 쉽고 유지관리할 수 없는 코드

- 해결책
  - 각 컴포넌트의 공유상태를 추출하여 전역에서 참조할 수 있는 저장소에서 관리
  - 중앙저장소_Pinia
  - 컴포넌트 트리는 하나의 큰 view가 되고 모든 컴포넌트는 트리 계층구조에 관계없이 상태에 접근하거나 기능을 사용할 수 있음

## Pinia
- Vue 공식 상태관리 라이브러리
- 프로젝트 빌드 시 Pinia 라이브러리 추가
  - stores 폴더 신규 생성
- 구성요소
  - store: 중앙 저장소. 모든 컴포넌트가 공유하는 상태, 기능 등이 작성됨
    - defineStore()의 반환값의 이름은 use와 store를 사용하는 것을 권장. 첫번째 인자는 store의 고유 Id
    - state: 반응형 상태(데이터), ref()===state
    - getters: 계산된 값. computed() == getters
    - actions:메서드, function() === actions
  - plugin
    - setup Stores: pinia의 상태들을 사용하려면 반드시 반환. store에서는 private한 상태속성을 가지지 않음

- 구성요소 활용
  - state: 각 컴포넌트 깊이에 관계없이 store 인스턴스로 state에 접근하여 직접 읽고 쓸 수 있음. 만약 store에 state를 정의하지 않았다면 컴포넌트에서 새로 추가할 수 없음.
 App.vue
```js
import {useCounterStore} from '@/stores/counter'

const store = useCounterStore()
const newNumber = store.count + 1
```
  - 템플릿에서 {{store.count}}같이 사용
  - getters도 똑같
  - actions도 똑같. store.increment() 상태자체 변경을 위해선 action 사용

## Pinia 실습
- 컴포넌트 구성
  - App
    - TodoForm
    - TodoList
      - TodoListItem
- 조회
  - counter.js
  -  const todos ref([
  -  {id:id++,text:'할 일1',isDone:false
  -  }])
  -  참조, const store = useCounterStore()

- create Todo
  - todos 목록에 addTodo 액션 정의. push
  - TodoForm에서 실시간으로 입력되는 사용자 데이터를 양방향 바인딩하여 반응형 변수로 할당
  - submit 이벤트 발생시 addTodo 호출
  - input 데이터 초기화 할 수 있도록 처리. form에 반응형 데이터 연결

- Delete Todo
  - 따로 정의하는 게 아니라 store.deleteTodo로도 연결 가능
```js
const deleteTodo = function (todoId) {
  const index = todos.value.findindex((todo) => todo.id ===todoId)
  todos.value.splice(index, 1)
}
// todos에서 특정 인덱스 todo삭제후 새로운 todos 배열로 교체
```

- Update Todo
  - isDone 속성값 반대로 재할당 후 새로운 todo 목록 반환
```js
const updateTodo = function (todoId) {
  todos.value = todos.value.map((todo) => {
    if (todo.id === todoId) {
      todo.isDone = !todo.isDone
    }
    return todo
  })
}
```

```js
const doneTodosCount = computed(() => {
  const doneTodos = todos.value.filter((todos) => todo.isDone)
  return doneTodos.length
})
```

- plugin_local storage
  - 설치
  - main.js에 등록
  - defineStore()의 3번째인자로 관련객체 추가