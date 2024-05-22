<template>
  <div class="main-container">
    <div class="sub-container">
      <section>
        <div>
          <h1 style="color: black;">회원님을 위한 영화추천</h1>
          <div class="recommend-box">
            <Carousel :autoplay="3000" :wrap-around="true" :pause-autoplay-on-hover="true" :breakpoints="breakpoints">
              <Slide v-for="movie in recommendMovies" :key="movie.id">
                <div class="carousel__item">
                  <RouterLink :to="{ name: 'MovieDetail', params: { movie_id: movie.id } }">
                    <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" class="poster-img">
                  </RouterLink>
                </div>
              </Slide>
              <template #addons>
                <Navigation />
                <Pagination />
              </template>
            </Carousel>
          </div>
        </div>

        <div class="recommend-box">
          <h1 style="color: black;">{{ genre }} 영화추천</h1>
          <Carousel :autoplay="3000" :wrap-around="true" :pause-autoplay-on-hover="true" :breakpoints="breakpoints">
            <Slide v-for="movie in recommendMovies_for_genre" :key="movie.id">
              <div class="carousel__item">
                <RouterLink :to="{ name: 'MovieDetail', params: { movie_id: movie.id } }">
                  <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" class="poster-img">
                </RouterLink>
              </div>
            </Slide>
            <template #addons>
              <Navigation />
              <Pagination />
            </template>
          </Carousel>
        </div>
      </section>

      <section>
        <div>
          <NowPlayingMovies />
        </div>

        <div class="map-box">
          <KakaoMap />
        </div>
        <div class="ranking-box">
          <UserRanking />
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { Carousel, Slide, Navigation, Pagination } from 'vue3-carousel';
import NowPlayingMovies from '@/components/NowPlayingMovies.vue'
import KakaoMap from '@/components/KakaoMap.vue';
import UserRanking from '@/components/UserRanking.vue';
import 'vue3-carousel/dist/carousel.css';
import { useMemberStore } from '@/stores/member';

const MemberStore = useMemberStore()

const movie = ref(null);
const recommendMovies = ref([]);
const recommendMovies_for_genre = ref([]);
const genre = ref(null)
const router = useRouter();

const fetchRecommendMovies = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/v1/recommend_movieList/', {
      headers: {
        'Authorization': `Token ${MemberStore.token}`
      }
    });
    recommendMovies.value = response.data;
  } catch (error) {
    console.error(error);
  }
};
// axios.put 으로는 특정 장르의 영화데이터들을 가져오기.
const fetchRecommendMovies_genre = async () => {
  try {

    console.log('Fetching recommended movies');
    console.log('Token:', MemberStore.token);
    const response = await axios.put('http://127.0.0.1:8000/api/v1/recommend_movieList/',
      {},
      {
        headers: {
          'Authorization': `Token ${MemberStore.token}`
        }
      });
    console.log('Response:', response.data)

    recommendMovies_for_genre.value = response.data.movies;
    genre.value = response.data.genre_chosen.name
  } catch (error) {
    console.error(error);
  }
};
// axios.put 으로는 특정 장르의 영화데이터들을 가져오기.
onMounted(() => {
  fetchRecommendMovies();
  fetchRecommendMovies_genre();
});





const breakpoints = [
  { width: 768, itemsToShow: 1.5 },
  { width: 1024, itemsToShow: 2.5 },
  { width: 1440, itemsToShow: 3.5 }
]
</script>

<style scoped>
.sub-container {
  display: flex;
  flex-direction: row;
}

.recommend-box {
  width: 768px;
}


.main-container {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}



.recommend-movie {
  background: rgba(39, 41, 50, 1);
  width: 800px;
  height: 400px;
  border-radius: 20px;
}

.carousel__item {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #333;
  border-radius: 10px;
  overflow: hidden;
}

.poster-img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.carousel__slide {
  padding: 10px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
}

.carousel__item:hover .poster-img {
  transform: scale(1.1);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s, box-shadow 0.3s;
}

.poster-img {
  transition: transform 0.3s, box-shadow 0.3s;
}

/* .map-box {
  flex-grow: 1; /* 남은 공간을 모두 차지하도록 함 */
/* } 

/* 다른 컴포넌트의 너비를 조절할 수 있습니다. */
/* 예를 들어 NowPlayingMovies 컴포넌트의 너비를 조절하려면 다음과 같이 작성할 수 있습니다. */
.ranking-box {
  width: 400px;
  /* 너비 조절 */
}
</style>
<!-- https://pedia.watcha.com/ko-KR/users/DgwxAeQYNxrMj/contents/movies/ratings -->