import Button from "./Button";
import "./DiaryList.css";
import DiaryItem from "./DiaryItem";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
const DiaryList = ({data}) => {

    const nav = useNavigate();
    const {sortType,setSortType} = useState("latest");

    const onChageSortType = (e) => {
        setSortType(e.target.value);
    };

    const getSortedData = () => {
        return data.toSorted((a, b) =>{
            if(sortType === "oldest") {
                return Number(a.createdDate) - Number(b.createdDate);
            } else {
                return Number(b.createdDate) - Number(a.createdDate);
            }
            });
        };
        // 원본배열은 그대로 냅두고 정렬된 새배열 반환
        // 사전순임에 유의
    const sortedData = getSortedData();

    // const sortedData = data.sort((a, b) => Number(b.createdDate) - Number(a.createdDate));
    // const sortedData = data.sort((a, b) => Number(a.createdDate) - Number(b.createdDate));
    
    return (
    <div className="DiaryList">
        <div className="menu_bar">
            <select> 
                <option value="latest">최신순</option>
                <option value="oldest">오래된 순</option>
            </select>
            <Button onClick={()=>nav("/new")} text={"새 일기 쓰기"} type={"POSITIVE"}/>
        </div>
        <div className="list_wrapper">
            {/* <DiaryItem /> */}
            {sortedData.map((item) => <DiaryItem key={item.id} {...item} /> )}
        </div>
    </div>
    )
};

export default DiaryList;