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
- 의존된 반응형데이터를 자동으로 추적
- 의존하는 데이터가 변경할 때만 재평가.
- computed vs method
  - 의존된 반응형 데이터를 기반으로 캐시_의존된 반응형 데이터가 변경될때만 <-> 랜더링 발생할 때마다 항상 함수 실행(항상 동일한 결과)
  - 캐시: 데이터나 결과를 일시적으로 저장해두는 임시 저장소
  - 이후 같은 데이터나 결과를 다시 계산하지않고 빠르게 접근할 수 있도록 함

## Conditional Rendering
- v-if,v-else,v-else-if
- <template 에 넣기> : 렌더링은 안됨
  - v-if vs v-show(일단 그림. 대신 히든으로 가림.온오프의 개념)