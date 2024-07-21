import Header from "../components/Header"
import Button from "../components/Button"
import Editor from "../components/Editor";
import { useNavigate} from "react-router-dom";
import { useContext,useEffect } from "react";
import { DiaryDispatchContext } from "../contexts/DiaryDispatchContext";
import usePageTitle from "../hooks/usePageTitle";

const New = () => {
    const {onCreateDiary} = useContext(DiaryDispatchContext);
    const nav = useNavigate();
    usePageTitle("새 일기 쓰기");
    
    const onSubmit = (input) => {
        onCreate(input.createdDate.getTime(), input.emotionId, input.content);
        nav("/", {replace: true});
        // 메인으로 리다이렉트, 그리고 뒤로가기해도 여기로 이동 x
    };
    return (
    <div>
        <Header title={"새 일기 쓰기"} 
        leftChild={<Button 
            onClick={()=>nav(-1)}
            // navigate 함수에 -1 인수를 주면 뒤로감
            text={"< 뒤로가기"}/>}
        />
        <Editor onSubmit={onSubmit} />
    </div>);
};

export default New;