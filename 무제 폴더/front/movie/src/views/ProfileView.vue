<template>
  <div class="content">
    <div v-if="memberStore.profile !== null">
      <h1>{{ memberStore.profile.nickname }}님의 프로필 페이지</h1>

      <div>
        <h2>좋아요를 누른 영화</h2>
        <div class="like-movie-container">
          <ul v-for="movie in likeMovies" :key="movie.id">
            <RouterLink :to="{ name: 'MovieDetail', params: { movie_id: movie.id } }" class="movie-info">
              <div>
                <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="Movie Poster" class="poster">
              </div>
              <div class="movie-text">
                <h3>{{ movie.title }}</h3>
                <p>
                  <span v-for="genreId in movie.genres" :key="genreId">
                    <span v-if="getGenreNameById(genreId)">{{ getGenreNameById(genreId) }}/ </span>
                  </span>
                </p>
                <p>{{ movie.overview }}</p>
              </div>
            </RouterLink>
          </ul>
        </div>
      </div>
    </div>

    <p v-else>로딩중...</p>
    <div>
      <div v-if="memberStore.loginUser === nowPageUser">
        <RouterLink :to="{ name: 'UpdateProfile', params: { username: memberStore.loginUser } }"><button>회원정보 수정</button></RouterLink>
        <button @click="deleteUser">회원탈퇴</button>
      </div>

      <div>
        <div class="trashes">
          <div>
            <NowPlayingMovies />
          </div>
          <div class="ranking-box">
            <UserRanking />
          </div>
          <div class="map-box">
            <KakaoMap />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useMemberStore } from '@/stores/member';
import { useRoute, useRouter, RouterLink, RouterView } from 'vue-router';
import NowPlayingMovies from '@/components/NowPlayingMovies.vue';
import KakaoMap from '@/components/KakaoMap.vue';
import UserRanking from '@/components/UserRanking.vue';
import axios from 'axios';

const route = useRoute();
const router = useRouter();
const nowPageUser = ref();
const memberStore = useMemberStore();
const likeMovies = ref([]);
const likeGenres = ref([]);

const getGenreNameById = function (genreId) {
  const genre = likeGenres.value.find(g => g.id === genreId)
  return genre ? genre.name : ''
}

const getMovie = function() {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${movieId.value}/`
  })
    .then((response) => {
      likeMovies.value.push(response.data);
    })
    .catch(error => console.error(error));
};

const getGenres = function() {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/genres/'
  })
    .then(response => likeGenres.value = response.data)
    .catch(error => console.log(error))
};

const deleteUser = function() {
  axios({
    method: 'post',
    url: `${memberStore.API_URL}/profile/${nowPageUser.value}/`,
    headers: {
      Authorization: `Token ${memberStore.token}`
    }
  })
    .then((response) => {
      window.alert('정상적으로 회원탈퇴 되었습니다.');
      memberStore.logout();
    })
    .catch((error) => {
      router.push(`/profile/:${nowPageUser.value}`);
    });
};

onMounted(() => {
  nowPageUser.value = route.params.username;
  memberStore.getProfile();
  getGenres()
  memberStore.profile.like_movie.forEach(movieId => {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/${movieId}/`
    })
      .then((response) => {
        likeMovies.value.push(response.data);
      })
      .catch(error => console.error(error));
  });
});
</script>


<style scoped>
.content {
  color: black;
  display: flex;
  justify-content: space-evenly;
  margin-left: 100px;
}

.like-movie-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
}

.poster {
  height: 300px;
  width: 200px;
}

/* 기타 아이템들 */
.trashes {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}

.movie-text {
  display: flex;
  padding-left: 10px;
  flex-direction: column;
  justify-content: space-around;
}
.movie-info {
  display: flex;
  flex-direction: row;
  text-decoration: none;
  color: black; /* 기본 글씨 색 검은색 */
}

.movie-info:hover {
  text-decoration: none;
  color: black; /* 기본 글씨 색 검은색 */
}

.trashes div {
  flex: 1;
  margin: 10px;
}


</style>
