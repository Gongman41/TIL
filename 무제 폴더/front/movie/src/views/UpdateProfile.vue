<template>
  <div>
    <h1 class="title">회원 정보 수정</h1>
    <form @submit.prevent="updateProfile">
      <div>
        <label for="nickname" class="label">닉네임</label>
        <p><input type="text" id="nickname" name="nickname" class="input-box" v-model="nickname"></p>
      </div>

      <!-- <div>
        <label for="followings" class="label">팔로잉</label>
        <p><input type="text" id="followings" name="followings" class="input-box" v-model="followings"></p>
      </div> -->

      <div>
        <label for="like_genre" class="label">좋아하는 장르</label>
        <div v-for="genre in movieStore.genres" :key="genre.pk">
          <input type="checkbox" :id="genre.name" :value="genre.id" v-model="choosenGenres">
          <label :for="genre.name">{{ genre.name }}</label>
        </div>
      </div>

      <input type="submit" class="signup-button" value="수정하기">
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useMemberStore } from '@/stores/member'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'

const nickname = ref(null)
const router = useRouter()
const followings = ref(null)
const like_movie = ref(null)
const like_genre = ref(null)
const movieStore = useMovieStore()
const choosenGenres = ref([])
const profile = ref(null)

const memberStore = useMemberStore()

const updateProfile = function () {
  axios({
    method: 'put',
    url: `${memberStore.API_URL}/profile/${memberStore.loginUser}/`,
    headers: {
      Authorization: `Token ${memberStore.token}`
    },
    data: {
      nickname: nickname.value,
      followings: followings.value,
      like_movie: like_movie.value,
      like_genre: like_genre.value,
      like_genre: choosenGenres.value
    }
  })
    .then((response) => {
      window.alert('회원 정보가 변경되었습니다.')
      router.push({ name: 'Profile', params: { username: memberStore.loginUser } })
    })
    .catch((error) => {
      console.log('회원 정보 변경 실패:', error)
      window.alert('회원 정보 변경에 실패했습니다.')
    })
}


onMounted(() => {
  memberStore.getProfile()
  nickname.value = memberStore.profile.nickname
  followings.value = memberStore.profile.followings
  like_movie.value = memberStore.profile.like_movie
  like_genre.value = memberStore.profile.like_genre
})
</script>

<style scoped>
.background-container {
  width: 100vw;
  /* 전체 화면 너비 */
  height: 100vh;
  /* 전체 화면 높이 */
  background-image: url('@/assets/background.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: black;
}

.title {
  color: black;
  font-size: 32px;
  margin-bottom: 20px;
}

.signup-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  padding: 20px;
  border-radius: 10px;
}

.label {
  font-size: 20px;
  font-weight: bold;
  color: black;
}

.input-box {
  background: rgba(26, 28, 38, 0.8);
  /* 살짝 투명하게 설정 */
  color: white;
  font-size: 20px;
  width: 300px;
  height: 40px;
  border-radius: 10px;
  padding-left: 10px;
  margin-bottom: 10px;
}

.signup-button {
  background: linear-gradient(to bottom, #763DCF, #5C24CC);
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