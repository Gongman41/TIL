<template>
  <div v-if="finalWinner" class="movie-container">
    <div v-if="finalWinner.poster_path !== undefined">
      <h2>Winner</h2>
      <p>{{ finalWinner.title }}</p>
      <img :src="`https://image.tmdb.org/t/p/w500${finalWinner.poster_path}`" alt="" class="poster-img">
    </div>

    <div v-else>
      <h2>Winner</h2>
      <p>{{ finalWinner }}</p>
    </div>
  </div>
  <div v-else>
    <p v-if="!movies">로딩중...</p>
    <div v-else>
      <div class="movie-container">
        <div class="poster-box">
          <div class="image-container" @click="video1 = !video1">
            <img v-if="movies[idx]?.poster_path" :src="`https://image.tmdb.org/t/p/w500${movies[idx].poster_path}`"
              class="poster-img">
            <img src="@/assets/yotube.png" class="youtube-button" />
            <MoviePreview v-if="video1 === true" :movie-title="movies[idx]?.title" />
          </div>
          <button @click="selectMovie(movies[idx])" class="choice-button">
            선택
          </button>
        </div>
        <h1>vs</h1>

        <div class="poster-box">
          <div class="image-container" @click="video2 = !video2">
            <img v-if="movies[idx + 1]?.poster_path"
              :src="`https://image.tmdb.org/t/p/w500${movies[idx + 1].poster_path}`" class="poster-img">
            <img src="@/assets/yotube.png" class="youtube-button" />

            <MoviePreview v-if="video2 === true" :movie-title="movies[idx + 1]?.title" />
          </div>
          <button @click="selectMovie(movies[idx + 1])" class="choice-button">
            선택
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { useMemberStore } from '@/stores/member';
import MoviePreview from '@/components/MoviePreview.vue'
import { onBeforeRouteLeave } from 'vue-router';
import axios from 'axios';

const store = useMovieStore();
const memberStore = useMemberStore()
const idx = ref(0);
const movies = ref([]);
const selectedMovies = ref([]);
const finalWinner = ref(null);
const video1 = ref(false)
const video2 = ref(false)

const shuffleArray = (array) => {
  return array.sort(() => Math.random() - 0.5);
};

const getRandomMovies = (movies, count) => {
  const shuffled = shuffleArray([...movies]);
  return shuffled.slice(0, count);
};

const startNextRound = () => {
  if (selectedMovies.value.length === 1) {
    finalWinner.value = selectedMovies.value[0];
  } else {
    movies.value = shuffleArray(selectedMovies.value);
    idx.value = 0;
    selectedMovies.value = [];
  }
};

const selectMovie = (movie) => {
  selectedMovies.value.push(movie);
  idx.value += 2;
  video1.value = false
  video2.value = false
  if (idx.value >= movies.value.length) {
    startNextRound();
  }
};

onMounted(() => {
  store.getMovies();
  movies.value = getRandomMovies(store.movies, 16);
  console.log(movies.value)
});

watch(finalWinner, (newValue) => {
  if (newValue !== null) {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/api/v1/likemovie/${newValue.id}/`,
      headers: {
        Authorization: `Token ${memberStore.token}`
      }
    })
      .then(res => console.log(res))
      .catch(err => console.log(err))
  }
})

onBeforeRouteLeave(() => finalWinner.value = null)
</script>

<style scoped>
button {
  padding: 10px;
  font-size: 16px;
  margin: 10px;
}

.movie-container {
  display: flex;
  width: 100vw;
  height: 100vh;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 100px;
}

.poster-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.poster-img {
  width: 100%;
  height: 100%;
}

.image-container {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

.youtube-button {
  position: absolute;
  opacity: 70%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  border-radius: 5px;

  width: 20%;
  border-radius: 30%;
}

.choice-button {
  background-color: rgb(224, 82, 82);
  font-weight: 700;
  margin: 0;
  width: 100%;
}
</style>
