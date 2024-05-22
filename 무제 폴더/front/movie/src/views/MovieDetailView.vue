<template>
  <div>
    <!-- <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" class="poster-img"> -->
    <div class="movie-box" v-if="movie !== null">
<!-- 
      <div v-if="videoId" class="video-wrapper">
        <iframe
          :src="`https://www.youtube.com/embed/${videoId}?autoplay=1&mute=1&controls=1&loop=1&playlist=${videoId}&playsinline=1`"
          frameborder="0" allowfullscreen class="video-frame"></iframe>
      </div> -->
      <h1 style="text-align: center; margin-top: 5%; " v-if="movie !== null">{{ movie.title }}</h1>
      
      <div class="movie-detail">
        <iframe v-if="videoId" style="width: 64vw; height: 60vh;"
        :src="`https://www.youtube.com/embed/${videoId}?autoplay=1&mute=1&controls=1&loop=1&playlist=${videoId}&playsinline=1`"
        frameborder="0" allowfullscreen></iframe>
        <p>장르 : {{ genres }}</p>
        <p>개봉 : {{ movie.release_date }}</p>
        <p>평점 : {{ movie.vote_average }}</p>
        <p>인기도 : {{ movie.popularity }}</p>
        <p @click="addLikeMovie(movie.id)">
          <p v-if="liked" @click="liked=!liked">좋아요 ♥</p>
          <p v-else @click="liked=!liked">좋아요 ♡</p>
        </p>
        <p style="text-indent: 10px;">{{ movie.overview }}</p>

        <p>출연 :
          <span v-for="actor in actors" :key="actor.id" class="person-item">
            <img :src="`https://image.tmdb.org/t/p/w500${actor.poster_path}`" alt="NO IMAGE" class="person-img">
            <p>{{ actor.name }}</p>
          </span>
        </p>
        <p>제작 :
          <span v-for="producer in crews" :key="producer.id" class="person-item">
            <img :src="`https://image.tmdb.org/t/p/w500${producer.poster_path}`" alt="NO IMAGE" class="person-img">
            <p>{{ producer.name }}</p>
          </span>
        </p>
      </div>
      <div class="review-container">
        <!-- 리뷰 리스트 -->
        <div class="review-list">
          <h2>리뷰 리스트</h2>
          <!-- 리뷰가 있는 경우에만 표시 -->
          <div v-if="reviews.length > 0">
            <div v-for="(review) in reviews" :key="review.id" class="review-item">
              <!-- <p>번호: {{ index }}</p> -->
              <p>{{ review.user.nickname }}</p>
              <p>{{ review.content }}</p>
              <!-- <p>좋아요: {{ review.rank }}/5</p> -->
              <p>{{ format(review.updated_at, 'yyyy-MM-dd') }}</p>

            </div>
          </div>
          <!-- 리뷰가 없는 경우 -->
          <p v-else>리뷰가 없습니다.</p>
        </div>

        <!-- 리뷰 작성 폼 -->
        <div class="review-form">
          <form @submit.prevent="submitReview">
            <label for="review-content">리뷰 내용:</label><br>
            <textarea id="review-content" v-model="newReview.content"></textarea><br>
            <label for="review-rating">평점 (1-5):</label><br>
            <input type="number" id="review-rating" v-model="newReview.rank" min="1" max="5"><br>
            <button type="submit">작성 완료</button>
          </form>
        </div>
      </div>
    </div>
    <p v-else>로딩중...</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useMemberStore } from '@/stores/member'
import { format } from 'date-fns';

const store = useMemberStore()
// const user = store.loginUser
// const reviews = ref([]); // 리뷰 리스트
const reviews = ref([])


const newReview = ref({ // 새로운 리뷰를 위한 데이터
  content: '',
  rank: ''
});
const route = useRoute()
const movieId = ref(null)
const movie = ref(null)
const videoId = ref(null)
const genres = ref('')
const actors = ref([])
const crews = ref([])
const liked = ref(false)

onMounted(() => {
  movieId.value = route.params.movie_id;
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${movieId.value}/`
  })
    .then((response) => {
      movie.value = response.data;
      submitQuery();
      return axios.get(`http://127.0.0.1:8000/api/v1/${movieId.value}/review/`); // 리뷰 목록 가져오기
    })
    .then((reviewsResponse) => {
      movie.value.liked_users.forEach(user => {
        if (user.username === store.loginUser) {
         liked.value = true 
        }
      })
      reviews.value = reviewsResponse.data;
    })
    .catch(error => console.error(error));
});

const addLikeMovie = function (movieId) {
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/api/v1/likemovie/${movieId}/`,
    headers: {
        'Authorization': `Token ${store.token}`
      }
  })
    .then(response => console.log(response))
    .catch(error => console.log(error))
}

const submitReview = async function () {
  try {
    const response = await axios.post(`http://127.0.0.1:8000/api/v1/${movieId.value}/review/`, {
      content: newReview.value.content,
      rank: newReview.value.rank,
    }, {
      headers: {
        'Authorization': `Token ${store.token}` // 인증 토큰 추가. Token으로 붙여야됨
      }
    });
    console.log(response)
    console.log(reviews.value)
    reviews.value.push(response.data);

    newReview.value.content = '';
    newReview.value.rank = '';
    console.log(reviews.value)
  } catch (error) {
    console.error(error.response ? error.response.data : error.message);
  }
}
// 같은 유저가 같은 작품에 리뷰 남겼을 때 문제발생

const submitQuery = async function () {
  try {
    const response = await axios({
      method: 'get',
      url: 'https://www.googleapis.com/youtube/v3/search',
      params: {
        part: 'snippet',
        q: `${movie.value.title} official trailer`,
        type: 'video',
        key: 'AIzaSyDskhfMipluROAa1aw94rdNHj4WrrIKHY4',
      }
      // key 갱신 문제
    });
    if (response.data.items.length > 0) {
      videoId.value = response.data.items[0].id.videoId
    } else {
      console.log('No video found')
    }

    const genresResponse = await Promise.all(movie.value.genres.map(getGenreName));
    genres.value = genresResponse.join(', ');

    const actorResponse = await Promise.all(movie.value.cast.map(getPerson));
    actors.value = actorResponse;

    const crewResponse = await Promise.all(movie.value.crew.map(getPerson));
    crews.value = crewResponse;
  } catch (error) {
    console.error(error);
  }
}

const getPerson = async function (PersonId) {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/${PersonId}/person/`);
    return response.data
  } catch (error) {
    console.log(error);
    return ''; // 에러가 발생하면 빈 문자열 반환
  }
}

const getGenreName = async function (genreId) {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/${genreId}/genre/`);
    return response.data.name;
  } catch (error) {
    console.log(error);
    return ''; // 에러가 발생하면 빈 문자열 반환
  }
}


</script>

<style scoped>
.movie-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.video-wrapper {
  position: absolute;
  width: 64vw;
  /* 브라우저 창 너비의 80% */
  padding-top: 36%;
  /* 가로 너비의 50%인 세로 비율 */
  margin: 0 auto;
  /* 가운데 정렬 */
}

.video-frame {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.movie-detail {
  width: 64vw;
  /* 브라우저 창 너비의 80% */
  padding-top: 5%;
  /* 가로 너비의 50%인 세로 비율 */
  margin: 0 auto;
  /* 가운데 정렬 */
}

.movie-detail>p {
  background: rgba(39, 41, 50, 1);
  color: white;
  font-size: 20px;
  padding: 15px 20px;
  /* 상하 15px, 좌우 20px */
  display: flex;
  flex-wrap: wrap;
  /* Flex wrap을 사용하여 요소들을 줄 바꿈 */
  line-height: 1.5;
  /* 줄 간격을 1.5로 설정 */

}


.person-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 10px;
  /* 적당한 거리 */
}

.person-img {
  width: 100px;
  /* 적당한 크기 */
  height: auto;
  border-radius: 10px;
  /* 이미지 테두리 둥글게 */
}

.review-container {
  position: relative;
  width: 64vw;
  /* 브라우저 창 너비의 80% */
  margin: 20px auto;
  /* 위아래 여백을 조정하여 가깝게 배치 */
  background: rgba(39, 41, 50, 1);
  color: white;
  font-size: 20px;
  /* border-radius: 20px; */
  padding: 15px 20px;
  /* 상하 15px, 좌우 20px */
  display: flex;
  flex-wrap: wrap;
  /* Flex wrap을 사용하여 요소들을 줄 바꿈 */
  line-height: 1.5;
  /* 줄 간격을 1.5로 설정 */
  flex-direction: column;
}

.review-list,
.review-form {
  flex: 1;
  margin-right: 20px;
}

.review-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 20px;
  display: flex;
  flex-direction: row;
}

.review-item>* {
  flex: 2;


}

.review-item> :nth-child(2) {
  flex: 6;
  /* 중앙 요소의 너비 비율을 8로 설정 */
}

.review-form form {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.review-form label {
  flex: 2;
}

.review-form textarea {
  flex: 6;
}

.review-form input[type="number"] {
  flex: 2;

}

.review-form button {
  flex: 2;
}

</style>
