<template>
  <div>
    <nav v-if="memberStore.token !== null" class="navbar">
      <RouterLink to="/" :class="{ 'click': route.path === '/', 'non-click': route.path !== '/' }">
        <img v-if="route.path !== '/'" src="@/assets/home.png" alt="home">
        <img v-if="route.path === '/'" src="@/assets/click_home.png" alt="home">
      </RouterLink>

      <RouterLink to="/dongjinlove"
        :class="{ 'click': route.path === '/dongjinlove', 'non-click': route.path !== '/dongjinlove' }">
        <img v-if="route.path !== '/dongjinlove'" src="@/assets/game.png" alt="game">
        <img v-if="route.path === '/dongjinlove'" src="@/assets/click_game.png" alt="game">
      </RouterLink>



      <RouterLink to="/movieworldcup">
        <img v-if="route.name !== 'WorldCup'" src="@/assets/trophy.png" alt="trophy">
        <img v-if="route.name === 'WorldCup'" src="@/assets/click_trophy.png" alt="trophy">
      </RouterLink>

      <RouterLink :to="{ name: 'Profile', params: { username: memberStore.loginUser } }"
        :class="{ 'click': route.name === 'Profile', 'non-click': route.name !== 'Profile' }">
        <img v-if="route.name !== 'Profile'" src="@/assets/profile.png" alt="profile">
        <img v-if="route.name === 'Profile'" src="@/assets/click_profile.png" alt="profile">
      </RouterLink>

      <div>
        <form @submit.prevent="search">
          <input type="text" v-model="movie" id="movie" class="input-box" placeholder="영화 검색">
        </form>
      </div>

      <button @click="logout" class="logout-button">로그아웃</button>
    </nav>

    <nav v-else class="navbar">
      <RouterLink to="/signup">회원가입</RouterLink> |
      <RouterLink to="/login">로그인</RouterLink>
    </nav>


    <RouterView />

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, RouterView, RouterLink } from 'vue-router'
import { useMemberStore } from '@/stores/member';
import axios from 'axios';

const route = useRoute()
const router = useRouter()
const memberStore = useMemberStore()
const movie = ref(null)
const logout = function () {
  memberStore.logout()
}

const search = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/v1/search/', {
      params: { movie_title: movie.value }
    });
    console.log(movie)
    router.push({
      path: `/search/${movie.value}`,
      query: {
        responseData: JSON.stringify(response.data) // response 데이터를 JSON 문자열로 변환
      }
    });;
  } catch (error) {
    console.error(error);
  }
};

!function (w, d, s, ...args) {
  var div = d.createElement('div');
  div.id = 'aichatbot';
  d.body.appendChild(div);
  w.chatbotConfig = args;
  var f = d.getElementsByTagName(s)[0],
    j = d.createElement(s);
  j.defer = true;
  j.type = 'module';
  j.src = 'https://aichatbot.sendbird.com/index.js';
  f.parentNode.insertBefore(j, f);
}(window, document, 'script', 'A42A977B-F6E9-4454-BE34-03E57E0542A5', 'onboarding_bot', {
  apiHost: 'https://api-cf-ap-2.sendbird.com',
});

</script >


<style scoped>
img {
  width: 50px;
}

.input-box {
  background: #0a141e;
  color: white;
  font-size: 15px;
  width: 200px;
  height: 40px;
  border-radius: 20px;
  padding-left: 20px;
}


.click {
  background-color: #1a1c26;
  border-top-left-radius: 40%;
  border-bottom-left-radius: 40%;
}

.non-click {
  background: rgba(39, 41, 50, 1);
  /* border-top-left-radius: 40%;
  border-bottom-left-radius: 40%; */
}

.navbar {
  display: flex;
  justify-content: flex-end;
  /* 오른쪽으로 정렬 */
  align-items: center;
  /* 세로 중앙 정렬 */
  flex-direction: row;
  /* 수평으로 정렬 */
  background: rgba(39, 41, 50, 1);
  position: sticky;
}



.navbar a,
.navbar button {
  color: white;
  /* 텍스트 색상 */
  text-decoration: none;
  /* 밑줄 제거 */
  padding: 10px;
  /* 패딩 추가 */
}

.navbar a:hover,
.navbar button:hover {
  background-color: #1a1c26;
  /* 마우스 오버 시 배경색 변경 */
}

.logout-button {
  /* background: linear-gradient(to bottom, #625477, #322846); */
  background-color: #5E31A6;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-left: 10px;
  /* 버튼을 오른쪽으로 이동 */
}

.navbar img:hover {
  filter: brightness(0.8);
}
</style>
