import "./DiaryItem.css";
import Button from "./Button";
import  {getEmotionImages} from "../util/get-emotion-image";
import { useNavigate } from "react-router-dom";
const DiaryItem = ({id,emotionId,createdDate,content}) => {

    const nav = useNavigate();
    return (
    <div className="DiaryItem">
        <div 
        onClick={() => nav(`/diary/${id}`)} 
        className={`img_section img_section ${emotionId}`}>
            <img src={getEmotionImages(emotionId)}/>
        </div>
        <div 
        onClick={() => nav(`/diary/${id}`)} 
        className="info_section">
            <div className="created_date">
                {new Date(createdDate).toLocalDateString()}
            </div>
            <div className="content">
                {content}
            </div>
        </div>
        <div className="button_section">
            <Button 
            onClick={() => nav(`/edit/${id}`)} 
            text={"수정하기"}/>
        </div>
    </div>
    );
};

export default DiaryItem;