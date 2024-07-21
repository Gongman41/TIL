
import './App.css'
// import {Rounts,Route,Link,useNavigate} from "react-router-dom";
import {Rounts,Route} from "react-router-dom";
import { useReducer,useRef,createContext, useEffect } from 'react';
// a 태그 대체용, 페이지를 실제로 이동하는 navigate함수 반환
import Home from './pages/Home';
import Diary from './pages/Diary';
import New from './pages/New';
import NotFound from './pages/NotFound';
// import {getEmotionIcon} from "./utils/get-emotion-Image";
// import Button from './components/Button';
//import Header from './components/Header';
import Edit from './pages/Edit';


function reducer(state, action) {
  let nextState;

  switch(action.type) {
    case "INIT": {
      return action.data;
    }
    case "CREATE":
      { nextState = [action.data,...state];
        break;
      }
    case "UPDATE":
      {nextState = state.map((item) => String(item.id) === String(action.data.id)? action.data : item);
          break;
      }
    case "DELETE":
      {nextState = state.filter((item) => String(item.id)!== String(action.id));
        break;
      }
    default:
      return state;
    
  };
  localStorage.setItem('diary', JSON.stringify(nextState));
  return nextState;
}

export const DiaryStateContext = createContext();
export const DiaryDispatchContext = createContext();
function App() {
// / 모든 일기를 조회하는 Home ㅠㅔ이지
// /new 새로운 일기 작성
// /diary 상세조회
  // const nav = useNavigate();
  // const onClick = () => {
  //   nav('/new');
  // };
  const [isLoading, setIsLoading] = useState(true);
  const {data,dispatch} = useReducer(reducer, []);
  const idRef = useRef(0);
  // 새로운 일기 추가
  // localStorage.setItem('test',"hello");
  // value로 객체 저장 시 문자열로 변환.  Json.stringify({name:"이정환"});
  // 객체 호출 시 JSON.parse(localStorage.getItem('person')); 인수로 전달한 값이 undefined이거나 null일 경우 에러 발생
  // localStorage.removeItem('person');

  useEffect(() => {
    const storedData = JSON.parse(localStorage.getItem('diary'));
    if (!storedData) {
      return;
    }
    const parsedData = JSON.parse(storedData);
    if (!Array.isArray(parsedData)) {
      setIsLoading(false);
      return;
    };

    let maxId = 0;
    parsedData.forEach((item) => {
      if (Number(item.id) > maxId) {
        maxId = Number(item.id);
      }
    });
    idRef.current = maxId + 1;
    // parsedData 가 배열이 아닐 경우
    dispatch({
      type: "INIT",
      data: parsedData,
    });
    setIsLoading(false);
  },[])
  const onCreate = (createdDate,emotionId,content) => {
    dispatch({
      type:"CREATE",
      data:{
      id : idRef.current++,
      createdDate,
      emotionId,
      content
      },
    });

  };
  // 기존 일기 수정
  const onUpdate = (createdDate,emotionId,content) => {
    dispatch({
      type:"UPDATE",
      data:{
        id : idRef.current++,
        createdDate,
        emotionId,
        content
      },
    });

  };
  // 기존 일기 삭제

  const onDelete = (id) => {
    dispatch({
      type:"DELETE",
      data:{
        id
      },
    });

  };

  if (isLoading) {
    return <div>Loading...</div>;
  }
  return (
    <>
    {/* <Header title={"Header"}
    leftChild={<Button text={"Left"}/>}
    rightChild={<Button text={"Right"}/>}
    />
    <Button 
    // type={"DEFAULT"}
    text={"123"}
    onClick={()=> {
      console.log("123번 버튼 클릭!")
    }}/>
    <Button 
    type={"POSITIVE"}
    text={"123"}
    onClick={()=> {
      console.log("123번 버튼 클릭!")
    }}/>
    <Button 
    type={"NEGATIVE"}
    text={"123"}
    onClick={()=> {
      console.log("123번 버튼 클릭!")
    }}/> */}
    {/*<div>
      <img src="{getEmotionIcon(1)}" />
      <img src="{getEmotionIcon(2)}" />
      <img src="{getEmotionIcon(3)}" />
      <img src="{getEmotionIcon(4)}" />
      <img src="{getEmotionIcon(5)}" />
    </div>
    <div>
      <Link to={"/"}>Home</Link>
      <Link to={"/new"}>New</Link>
      <Link to={"/diary"}>Diary</Link>
      내부링크는 Link 사용
    </div> 
    <button>new 페이지로 이동</button>
    다른 컴포넌트로 이동시 navigate()사용. 이게 더 활용도가 높을듯*/}

  <DiaryStateContext.Provider value={data}>
    <DiaryDispatchContext.Provider value={{onCreate,onUpdate,onDelete}}>
    <Rounts>
      <Route path='/' element={<Home />} />
      <Route path='/new' element={<New />} />
      <Route path='/diary/:id' element={<Diary />} />
      {/* :뒤에 url파라미터 입력 */}
      <Route path='/edit/:id' element={<Edit/>}/>
      <Route path='*' element={<NotFound/>}/>
    </Rounts>
    </DiaryDispatchContext.Provider>
    </DiaryStateContext.Provider>
    {/* // 안에는 Route만 들어갈 수 있다.
    // Routes안에있는 요소들만 바뀌는 것. 다른 요소들은 공통으로 return됨 */}
    </>
  );
  
}

export default App;
