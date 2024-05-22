<template>
  <div class="background-container bg-img">
    <form @submit.prevent="signup" class="signup-form">
      <div>
        <div style="border-bottom: 1px solid red; width: 100%; text-align: center;">
          <h1 class="title">회원가입 페이지</h1>
        </div>
        <div>
          <p><label for="username" class="label">아이디</label></p>
          <input type="text" v-model.trim="username" id="username" class="input-box">
        </div>
        <div>
          <p><label for="password1" class="label">비밀번호</label></p>
          <input type="password" v-model.trim="password1" id="password1" class="input-box">
        </div>
        <div>
          <p><label for="password2" class="label">비밀번호 확인</label></p>
          <input type="password" v-model.trim="password2" id="password2" class="input-box">
        </div>
        <div>
          <p><label for="nickname" class="label">닉네임</label></p>
          <input type="text" v-model.trim="nickname" id="nickname" class="input-box">
        </div>
      </div>

      <div v-for="genre in movieStore.genres" :key="genre.pk">
        <input type="checkbox" :id="genre.name" :value="genre.id" v-model="choosenGenres">
        <label :for="genre.name">{{ genre.name }}</label>
      </div>

      <input type="submit" value="회원가입" class="signup-button">
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMemberStore } from '@/stores/member'
import { useMovieStore } from '@/stores/movie'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const memberStore = useMemberStore()
const movieStore = useMovieStore()
const choosenGenres = ref([])

const signup = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    like_genre: choosenGenres.value
  }
  memberStore.signup(payload)
}

onMounted(() => {
  movieStore.getGenres()
})
</script>

<style scoped>
.background-container {
  width: 100vw;
  /* 전체 화면 너비 */
  height: 100vh;
  /* 전체 화면 높이 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  color: #3D3D3D;
}

.bg-img {
  background-image: url('@/assets/dong.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  background-color: #f5f7fe;
}

.title {
  color: white;
  font-size: 32px;
  margin-bottom: 20px;
}

.signup-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #af787b;
  margin: 100px;
  /* background-color: rgba(0, 0, 0, 0.5); */
  padding: 20px;
  border-radius: 10px;
}

.label {
  font-size: 20px;
  font-weight: bold;
  color: white;
}

.input-box {
  background: #f5f7fe;
  color: black;
  font-size: 20px;
  width: 300px;
  height: 40px;
  border-radius: 10px;
  padding-left: 10px;
  margin-bottom: 10px;
}

.signup-button {
  /* background: linear-gradient(to bottom, #c9b6b4, #af787b); */
  background-color: red;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
  text-align: center;
  text-decoration: none;
}
</style>
