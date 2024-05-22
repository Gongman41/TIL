<template>
  <div class="movie-item">
    <RouterLink :to="{ name: 'MovieDetail', params: { movie_id: movie.id } }">
      <img 
        :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" 
        alt="Movie Poster" 
        class="poster-img"
      >
      <div class="movie-info">
      </div>
    </RouterLink>
  </div>
</template>
<script setup>
import { defineProps } from 'vue';
import { RouterLink } from 'vue-router';

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
});
</script>
<style scoped>
.movie-item {
  flex: 1 1 calc(25% - 16px); /* 기본적으로 한 줄에 4개의 아이템 */
  max-width: calc(25% - 16px);
  background-color: #f0f0f0;
  padding: 8px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.movie-item img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 8px;
}

.movie-info {
  margin-top: 8px;
  text-align: center;
}

@media (max-width: 1200px) {
  .movie-item {
    flex: 1 1 calc(33.33% - 16px); /* 화면이 중간 크기일 때 한 줄에 3개의 아이템 */
    max-width: calc(33.33% - 16px);
  }
}

@media (max-width: 900px) {
  .movie-item {
    flex: 1 1 calc(50% - 16px); /* 화면이 작을 때 한 줄에 2개의 아이템 */
    max-width: calc(50% - 16px);
  }
}

@media (max-width: 600px) {
  .movie-item {
    flex: 1 1 calc(100% - 16px); /* 화면이 매우 작을 때 한 줄에 1개의 아이템 */
    max-width: calc(100% - 16px);
  }
}
</style>
