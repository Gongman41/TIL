어플리케이션의 복잡성을 낮춰서 예측가능하게
Single Source of True
상태는 객체. 하나의 객체안에 필요한 모든 데이터를 우겨넣기, 중앙집중적으로 관리
단 하나의 상태를 유지하고 외부와 차단. 담당자만을 통해_특정 함수만을 통해 상태 수정. dispatcher, reducer로.
데이터 가져오는것도 getState()로만 가능.
상태값이 바뀔때마다 해당 상태만 렌더링?

UNDO REDO 가 쉬움. 원본은 그대로, 원본을 복제하고 수정해서 새로운 원본으로 만들기 때문에 독립된 상태 유지. 어플리케이션의 현재상태, 이전상태까지 확인 가능. 문제해결 쉬워짐. 
모듈, 리로딩 가능. 코드 작성 시 자동으로 애플리케이션에 반영
핫모듈리로딩_애플리케이션은 새로 리프레시, 데이터는 그대로이기 때문에, 다시 입력작업 필요 x

store(은행): 정보가 저장되는 곳.
    - state: 실제 정보,직접 접속 금지, 불가
    - reducer(): 
    ```js
    function reducer(oldState,action) {
        pass;
    }
    var store = Redux.createStore(reducer)
    ```
    - getState()
    - subScribe(): state값이 바뀔때마다 render 호출, UI갱신
    - dispatch(): action(객체)를 받아 reducer를 호출해서(현재 state, action 데이터 전달) state값을 바꾸고 subscribe로 render 호출. 
    복사본을 받아서 수정 후 리턴해야 시간여행 가능
render: 우리가 짤 코드. getState()로 상태값을 가져와서 render.



redux가 좋은 이유
redux tool. 크롬 개발자도구 툴, 이전상태, 현재상태 출력


 