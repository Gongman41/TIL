import {useParams, useNavigate} from "react-router-dom";
import Header from "../components/Header";
import Button from "../components/Button";
import Editor from "../components/Editor";
import { useContext, useEffect, useState } from "react";
import { DiaryDispatchContext, DiaryStateContext } from "../contexts/DiaryDispatchContext";
import useDiary from "../hooks/useDiary";


const Edit = () => {
    const params = useParams();
    // url의 params
    const nav = useNavigate();
    const {onDelete, onUpdate} = useContext(DiaryDispatchContext);
    const curDiaryItem = useDiary(params.id);
    
    const onClickDelete = () => {
        if(
        window.confirm("일기 ㄹㅇ루다가 삭제할꺼?")
        ) {
            onDelete(params.id);
            nav("/", {replace: true});
            // 이거는 이벤트 핸들러. 클릭 시 실행
        }

    };

    

    // const getCurrentDiaryItem = () => {
    //     const currentDiaryItem = data.find((item)=>String(item.id) === String(params.id));

    //     if (!currentDiaryItem) {
    //         window.alert("일기를 찾을 수 없습니다.");
    //         nav("/", {replace: true});
    //         // 컴포넌트 호출될 때 즉시 호출. 페이지가 다 마운트 된 다음에 호출되야한다

    //     }
    //     return currentDiaryItem;

    // };

    const currentDiaryItem = getCurrentDiaryItem();

    const onSubmit = (input) => {
        if (window.confirm("일기를 수정하시겠습니까?")) {
        onUpdate(params.id, input.createdDate.getTime(), input.emotionId, input.content);
        nav("/", {replace: true});
        };
        // 순서유의
    };
    return (
    <div>
        <Header 
        title={"일기 수정하기"}
        leftChild={<Button onClick={()=>nav(-1)} text={"< 뒤로 가기"}/>}
        rightChild={<Button text={"삭제하기"} type={"NEGATIVE"} onClick={onClickDelete}/>}
        />
        <Editor initData={curDiaryItem}/>
    </div>
);
};

export default Edit;

