import "./EmotionItem.css";
import {getEmtionImage} from "./Emotion

const EmotionItem = ({emotionId, emotionName, isSelected,onClick}) => {
    return (
        <div 
        onClick={onClick} 
        className={`EmotionItem ${isSelected ? `EmotionUtem)on_${emotionId}`:""}`}>
            <img className="emotion_img" src={getEmotionTmage(emotionId)} />
            <div className="emotion_name">{emotionName}</div>
        </div>
    );
};

export default EmotionItem;