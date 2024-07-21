import { useContext, useState, useEffect} from "react";
import {DiaryStateContext} from "../App"
import {useNavigate} from "react-router-dom";

const useDiary = (id) => {
    const data = useContext(DiaryStateContext);
    const [curDiaryItem,setCurDiaryItem] = useState();
    const nav = useNavigate();
    useEffect(()=> {
        const currentDiaryItem = data.find((item)=>String(item.id) === String(id));
    
            if (!currentDiaryItem) {
                window.alert("일기를 찾을 수 없습니다.");
                nav("/", {replace: true});
                // 컴포넌트 호출될 때 즉시 호출. 페이지가 다 마운트 된 다음에 호출되야한다
    
            }

            setCurDiaryItem(currentDiaryItem);
    },[id, data]);
    return curDiaryItem

};

export default useDiary;