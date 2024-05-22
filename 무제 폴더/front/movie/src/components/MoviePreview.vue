<template>
  <div class="modal" v-if="videoId">
    <span class="close" @click="closeModal">&times;</span>
    <iframe width="640" height="360"
      :src="`https://www.youtube.com/embed/${videoId}?autoplay=1&mute=1&controls=1&loop=1&playlist=${videoId}&playsinline=1`"
      frameborder="0" allowfullscreen></iframe>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue';
import axios from 'axios';

// props로 전달된 movieTitle 값을 받음
const props = defineProps({
  movieTitle: String
})
const movieTitle = ref(props.movieTitle)
const videoId = ref(null);

const closeModal = () => {
  videoId.value = null;
};

const submitQuery = function () {
  console.log(import.meta.env.VITE_YOUTUBE_API_KEY)
  axios({
    method: 'get',
    url: 'https://www.googleapis.com/youtube/v3/search',
    params: {
      part: 'snippet',
      q: `${movieTitle.value} official trailer`, // movieTitle을 검색어로 사용합니다.
      type: 'video',
      key: import.meta.env.VITE_YOUTUBE_API_KEY, // 여기에 본인의 YouTube API 키를 입력하세요.
    }
  })
    .then((response) => {
      // API 응답에서 첫 번째 동영상의 videoId를 가져옵니다.
      videoId.value = response.data.items[0].id.videoId;
      console.log(response.data.items)
      console.log(videoId.value)
    })
    .catch((error) => {
      console.log(error)
    })
}

// 컴포넌트가 마운트되면 검색을 자동으로 실행합니다.
onMounted(() => {
  submitQuery()
});
</script>

<style scoped>
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal .close {
  color: white;
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 24px;
  cursor: pointer;
}
</style>
