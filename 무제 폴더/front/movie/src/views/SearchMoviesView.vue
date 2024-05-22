<template>
  <div class="container">
  <h1>검색결과리스트</h1>
  <div class="movie-grid">
    <SearchMovieList v-if="movies" v-for="movie in movies" :key="movie.id" :movie="movie" />
  </div>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import SearchMovieList from '@/components/SearchMovieList.vue';
import { useRoute } from 'vue-router';

const movies = ref(null);
const route = useRoute();

onMounted(() => {
  movies.value = JSON.parse(route.query.responseData);
});
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* 컨테이너를 중앙에 정렬 */
  width: 80vw;
  margin: 0 auto; /* 컨테이너를 수평으로 중앙에 배치 */
}

.movie-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  padding: 16px;
}
.movie-grid > * {
  background-color: #f0f0f0;
  padding: 8px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  flex: 1 1 calc(25% - 16px); /* 화면이 넓을 때는 4개의 아이템을 한 줄에 배치 */
  max-width: calc(25% - 16px);
  aspect-ratio: 2 / 3; /* 2:3 비율을 유지하도록 설정 */
  overflow: hidden;
}

@media (max-width: 1200px) {
  .movie-grid > * {
    flex: 1 1 calc(33.33% - 16px); /* 화면이 중간 크기일 때는 3개의 아이템을 한 줄에 배치 */
    max-width: calc(33.33% - 16px);
  }
}

@media (max-width: 900px) {
  .movie-grid > * {
    flex: 1 1 calc(50% - 16px); /* 화면이 작을 때는 2개의 아이템을 한 줄에 배치 */
    max-width: calc(50% - 16px);
  }
}

@media (max-width: 600px) {
  .movie-grid > * {
    flex: 1 1 calc(100% - 16px); /* 화면이 매우 작을 때는 1개의 아이템을 한 줄에 배치 */
    max-width: calc(100% - 16px);
  }
}

</style>
