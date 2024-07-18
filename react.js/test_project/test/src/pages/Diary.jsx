import { useParams } from "react-router-dom";

// import { useSearchParams } from "react-router-dom";
const Diary = () => {
    // const {params, searchParams} = useParams();
    // params.get("value");
    const params = useParams();

    return <div> {params.id}</div>;
};

export default Diary;