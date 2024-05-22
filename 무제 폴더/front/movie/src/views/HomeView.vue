<template>
  <div v-if="done">
  <section class="firstSection">
    <div class="carousel">
      <div class="carousel-control-button left">
        <input type="radio" name="carousel-control-input">
      </div>
      <div class="carousel-control-button right">
        <input type="radio" name="carousel-control-input" checked>
      </div>
      <h1 style="color: white;">{{ memberStore.loginUser }}님 맞춤 추천 영화</h1>
      <div class="carousel-rotation-direction">
        <ul class="carousel-item-wrapper" :style="{ '--_num-elements': likeMovies.length }">
          <li v-for="(movie, index) in likeMovies" :key="index" class="carousel-item"
            :style="{ '--_index': index, '--_image-url': `url(https://image.tmdb.org/t/p/w500${movie.poster_path})` }">
            <RouterLink :to="{ name: 'MovieDetail', params: { movie_id: movie.id } }">{{ movie.title }}
            </RouterLink>
          </li>
        </ul>
      </div>
    </div>
    <img @click="scrollExactMatchesIntoView1" src="@/assets/down.png" class="arrow" />
  </section>



  <section class="secondSection">
    <img @click="scrollExactMatchesIntoView3" src="@/assets/up.png" class="arrow" />

    <div class="carousel">
      <div class="carousel-control-button left">
        <input type="radio" name="carousel-control-input">
      </div>
      <div class="carousel-control-button right">
        <input type="radio" name="carousel-control-input" checked>
      </div>
      <h1 style="color: white;">오늘의 영화 추천</h1>
      <div class="carousel-rotation-direction">
        <ul class="carousel-item-wrapper" :style="{ '--_num-elements': likeMovies.length }">
          <li v-for="(movie, index) in likeGenres" :key="index" class="carousel-item"
            :style="{ '--_index': index, '--_image-url': `url(https://image.tmdb.org/t/p/w500${movie.poster_path})` }">
            <RouterLink :to="{ name: 'MovieDetail', params: { movie_id: movie.id } }">{{ movie.title }}
            </RouterLink>
          </li>
        </ul>
      </div>
    </div>
    <img @click="scrollExactMatchesIntoView2" src="@/assets/down.png" class="arrow" />

  </section>
</div>

<div v-else>
  <p>로딩중...</p>
</div>
<!-- 
  <section>
    <div>
      <img @click="scrollExactMatchesIntoView3" src="@/assets/up.png" class="arrow" />
    </div>

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
  </section> -->
</template>



<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useMemberStore } from '@/stores/member';
import { useRoute, useRouter, RouterLink, RouterView } from 'vue-router';
import axios from 'axios';

const route = useRoute()
const router = useRouter()
const nowPageUser = ref()
const memberStore = useMemberStore()
const likeMovies = ref([])
const likeGenres = ref([])
const done = ref(false)


const getMovie = function () {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/recommend_movieList/`,
    headers: {
      Authorization: `Token ${memberStore.token}`
    }
  })
    .then((response) => {
      likeMovies.value = response.data
    })
    .catch(error => console.error(error));
}
const getLikeMovie = function () {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/recommend_movieListall/`,
    headers: {
      Authorization: `Token ${memberStore.token}`
    }
  })
    .then((response) => {
      likeGenres.value = response.data
      done.value = true
    })
    .catch(error => console.error(error));
}

const getGenreName = async function (genreId) {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/${genreId}/genre/`);
    likeGenres.value.push(response.data.name)
  } catch (error) {
    console.log(error);
  }
}

const scrollExactMatchesIntoView1 = () => {
  const centerElement = document.querySelector('.secondSection');
  if (centerElement) {
    centerElement.scrollIntoView({ behavior: 'smooth' });
  } else {
    setTimeout(scrollExactMatchesIntoView, 10)
  }
}
const scrollExactMatchesIntoView2 = () => {
  const centerElement = document.querySelector('.trashes');
  if (centerElement) {
    centerElement.scrollIntoView({ behavior: 'smooth' });
  } else {
    setTimeout(scrollExactMatchesIntoView, 10)
  }
}
const scrollExactMatchesIntoView3 = () => {
  const centerElement = document.querySelector('.firstSection');
  if (centerElement) {
    centerElement.scrollIntoView({ behavior: 'smooth' });
  } else {
    setTimeout(scrollExactMatchesIntoView, 10)
  }
}

onMounted(() => {
  nowPageUser.value = route.params.username
  console.log(memberStore.token)
  memberStore.getProfile()
  getMovie()
  getLikeMovie()
  // memberStore.profile.like_genre.forEach(genreId => getGenreName(genreId))
  // memberStore.profile.like_movie.forEach(movieId => {
  //   axios({
  //     method: 'get',
  //     url: `http://127.0.0.1:8000/api/v1/${movieId}/`
  //   })
  //     .then((response) => {
  //       likeMovies.value.push(response.data)
  //     })
  //     .catch(error => console.error(error));
  // })
})

onUnmounted(() => {
  done.value = false
})
</script>

<style>
.arrow {
  width: 30px;
}

section {
  display: flex;
  flex-direction: column;
}


/* :root 변수들을 전역으로 적용 */
:root {
  --carousel-transition-duration: 250ms;
  --carousel-transition-ease: ease-out;
  --carousel-bg-color-rgb: 10, 20, 30;
  --carousel-shadow-color-rgb: 128, 128, 128;
  --carousel-item-width: 11.5rem;
  --carousel-item-height: 17.5rem;
  --carousel-item-hover-effect: 1.075;
  --carousel-item-reflection-blur: 0.25rem;
  --carousel-item-empty-color-rgb: 255, 255, 255;
  --carousel-item-glow-color-rgb: 255, 255, 255;
  --carousel-item-glow-size: 5rem;
  --carousel-diameter: 50rem;
  --carousel-3d-perspective: 1000px;
  --carousel-3d-perspective-origin: 50% 20%;
  --carousel-control-button-width: 1.25rem;
  --carousel-control-button-height: 4rem;
  --carousel-control-color-rgb: 255, 255, 255;
  --carousel-animation-duration: 25s;
  --carousel-animation-play-state: running;
  --carousel-direction-animation-play-state: paused;
}

/* global styles */
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  border: 0;
  box-sizing: border-box;
}

*:focus {
  outline: none;
}

a {
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  -webkit-tap-highlight-color: transparent;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

section {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: rgb(var(--carousel-bg-color-rgb));
  overflow: hidden;
}

/* carousel */
.carousel {
  --_diameter: var(--carousel-diameter);
  --_radius: calc(var(--_diameter) / 2);
  --_item-width: var(--carousel-item-width);
  --_item-height: var(--carousel-item-height);
  perspective: var(--carousel-3d-perspective);
  perspective-origin: var(--carousel-3d-perspective-origin);
  width: var(--_diameter);
  height: var(--_diameter);
}

@media only screen and (max-width: 48rem) {
  .carousel {
    --_diameter: calc(var(--carousel-diameter) * 0.75);
    --_item-width: calc(var(--carousel-item-width) * 0.75);
    --_item-height: calc(var(--carousel-item-height) * 0.75);
  }
}

@media only screen and (max-width: 32rem) {
  .carousel {
    --_diameter: calc(var(--carousel-diameter) * 0.6);
    --_item-width: calc(var(--carousel-item-width) * 0.6);
    --_item-height: calc(var(--carousel-item-height) * 0.6);
  }
}

@media only screen and (max-width: 16rem) {
  .carousel {
    --_diameter: calc(var(--carousel-diameter) * 0.25);
    --_item-width: calc(var(--carousel-item-width) * 0.25);
    --_item-height: calc(var(--carousel-item-height) * 0.25);
  }
}

.carousel .carousel-control-button {
  --_width: var(--carousel-control-button-width);
  --_height: var(--carousel-control-button-height);
  z-index: 1;
  width: var(--_width);
  height: var(--_height);
  background-color: rgb(var(--carousel-control-color-rgb));
  opacity: 0.2;
  transition: opacity var(--carousel-transition-duration) var(--carousel-transition-ease);
  position: absolute;
}

.carousel .carousel-control-button:hover {
  opacity: 0.4;
}

.carousel .carousel-control-button:has(input:checked) {
  opacity: 0.8;
}

.carousel .carousel-control-button input {
  -webkit-appearance: none;
  appearance: none;
  opacity: 0;
  width: 100%;
  height: 100%;
  cursor: pointer;
}

.carousel .carousel-control-button.left {
  clip-path: polygon(0% 50%, 100% 0%, 100% 100%);
  top: calc(var(--_radius) - var(--_height) / 2);
  left: 0;
}

.carousel:has(.carousel-control-button.left input:checked) {
  --carousel-direction-animation-play-state: running;
}

.carousel .carousel-control-button.right {
  clip-path: polygon(0% 0%, 100% 50%, 0% 100%);
  top: calc(var(--_radius) - var(--_height) / 2);
  right: 0;
}

.carousel:has(.carousel-control-button.right input:checked) {
  --carousel-direction-animation-play-state: paused;
}

.carousel .carousel-rotation-direction {
  --_direction-animation-play-state: var(--carousel-direction-animation-play-state);
  --_z: calc(var(--_radius) * -1);
  transform: translateZ(var(--_z));
  transform-style: preserve-3d;
  animation: carousel-rotation-reverse calc(var(--carousel-animation-duration) / 2) reverse linear infinite var(--_direction-animation-play-state);
  transition: all var(--carousel-transition-duration) var(--carousel-transition-ease);
}

@keyframes carousel-rotation-reverse {
  from {
    transform: translateZ(var(--_z)) rotateY(0deg);
  }

  to {
    transform: translateZ(var(--_z)) rotateY(360deg);
  }
}

@keyframes carousel-rotation-normal {
  from {
    transform: rotateY(0deg);
  }

  to {
    transform: rotateY(360deg);
  }
}

.carousel .carousel-item-wrapper {
  transform-style: inherit;
  width: inherit;
  height: inherit;
  list-style-type: none;
  position: relative;
  animation: carousel-rotation-normal var(--carousel-animation-duration) normal linear infinite var(--carousel-animation-play-state);
  transition: all var(--carousel-transition-duration) var(--carousel-transition-ease);
}

.carousel .carousel-rotation-direction:has(.carousel-item:hover) {
  --carousel-animation-play-state: paused;
  --_direction-animation-play-state: paused;
}

.carousel .carousel-item {
  --_width: var(--_item-width);
  --_height: var(--_item-height);
  --_rotation: calc(360deg / var(--_num-elements) * var(--_index));
  left: calc(var(--_radius) - var(--_item-width) / 2);
  top: calc(var(--_radius) - var(--_item-height) / 2);
  transform: rotateY(var(--_rotation)) translateZ(var(--_radius));
  transform-style: inherit;
  width: var(--_width);
  height: var(--_height);
  transition: all var(--carousel-transition-duration) var(--carousel-transition-ease);
  box-shadow: 0 0 var(--carousel-item-glow-size) transparent;
  position: absolute;
}

.carousel .carousel-item:hover {
  box-shadow: 0 0 var(--carousel-item-glow-size) rgb(var(--carousel-item-glow-color-rgb));
  transform: rotateY(var(--_rotation)) translateZ(calc(var(--_radius) * var(--carousel-item-hover-effect)));
}

.carousel .carousel-item a {
  display: block;
  width: inherit;
  height: inherit;
  text-indent: -9999px;
  background-color: rgba(var(--carousel-item-empty-color-rgb), 0.5);
  background-image: var(--_image-url);
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  transition: filter var(--carousel-transition-duration) var(--carousel-transition-ease);
  filter: grayscale(100%);
}

.carousel .carousel-item:hover a {
  filter: grayscale(0%);
}

.carousel .carousel-item::before {
  content: '';
  width: inherit;
  height: inherit;
  background-color: rgba(var(--carousel-item-empty-color-rgb), 0.5);
  background-image:
    linear-gradient(to top, rgba(var(--carousel-bg-color-rgb), 0.25) 0%, rgba(var(--carousel-bg-color-rgb), 1.0) 75%),
    var(--_image-url);
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  pointer-events: none;
  filter: blur(var(--carousel-item-reflection-blur)) grayscale(100%);
  transition: filter var(--carousel-transition-duration) var(--carousel-transition-ease);
  transform-style: inherit;
  transform-origin: center bottom;
  transform: rotateX(90deg) rotateZ(180deg) rotateY(180deg);
  position: absolute;
}

.carousel .carousel-item:hover::before {
  filter: blur(var(--carousel-item-reflection-blur)) grayscale(0%);
}

.carousel .carousel-ground {
  --_width: var(--_diameter);
  --_height: var(--_diameter);
  --_rotation: 90deg;
  left: calc(var(--_radius) - var(--_width) / 2);
  top: calc(var(--_radius) - var(--_height) / 2);
  transform: rotateX(var(--_rotation)) translateZ(calc(var(--_item-height) / -2));
  width: var(--_width);
  height: var(--_height);
  border-radius: 50%;
  background: radial-gradient(rgba(var(--carousel-shadow-color-rgb), 0.75) 15%, rgba(var(--carousel-bg-color-rgb), 0) 60%);
  opacity: 0.5;
  transition: opacity var(--carousel-transition-duration) var(--carousel-transition-ease);
  position: absolute;
}

.carousel .carousel-item-wrapper:has(.carousel-item:hover) .carousel-ground {
  opacity: 0.75;
}
</style>
