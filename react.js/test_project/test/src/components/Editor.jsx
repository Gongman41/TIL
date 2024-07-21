import "./Editor.css";
import EmotionItem from "./EmotionItem";
import Button from "./Button";
import { useState, useEffect } from "react";
import {useNavigate } from "react-router-dom";
import { emotionList } from "../util/constants";
import { getStringedDate } from "../util/get-string-date";


const Editor = ({onSubmit, initData}) => {

    const nav = useNavigate();

    const [input,setInput] = useState({
        createdDate: new Date(),
        emotionId: 3,
        content: "",
    });

    useEffect(() => {
        if(initData){
            setInput({
                ...initData,
                createdDate: new Date(Number(initData.createdDate)),
            });
        }
})

    const onChangeInput = (e) => {
        // console.log(e.target.name);
        // console.log(e.target.value);

        let name = e.target.name;
        let value = e.target.value;
        if (name === "createdDate") {
            value = new Date(value);
        }

        setInput({
                   ...input,
                    // [e.target.name]: e.target.value 문자열로 들어옴
                    [name]: value,
                });
    }; 

    const onClickSubmitButton = () => {
        onSubmit(input);

    }
    return (
        <div className="Editor">
            <section className="date_section">
                <h4>오늘의 날짜</h4>
                <input 
                name="createdDate"
                onChange={onChangeInput}
                value={getStringedDate(input.createdDate)} type="date" />
            </section>
            <section className="emotion_section">
                <h4>오늘의 감정</h4>
                <div className="emotion_list_wrapper">
                   {emotionList.map((item)=> (
                    <EmotionItem 
                    onClick={()=>onChangeInput({
                        target: {
                            name: "emotionId",
                            value: item.emotionId,
                        },
                    })}
                    // 그냥 컴포넌트. 이벤트 객체가 알아서 전달되지 않음
                    key={item.emotionId} {...item} 
                    isSelected={item.emotionId === input.emotionId}/> ))}
                    
                </div>
            </section>
            <section className="content_section">
                <h4>오늘의 일기</h4>
                <textarea 
                name="content"
                value={input.content}
                onChange={onChangeInput}
                placeholder="오늘은 어땠나요?"/>
            </section>
            <section className="button_section">
                <Button 
                onClick={()=>nav(-1)}
                text={"취소하기"}/>
                <Button 
                text={"작성완료"}
                onClick={onSubmitButtonClick}
                type={"POSITIVE"}
                />
            </section>
        </div>
    )
};
// 새로고침은 App()이 다시 랜더링 된다는 뜻. 
export default Editor;