<template>
  <h2 style="color: black;">실시간 유저 랭킹</h2>
  <div class="user-ranking">

    <table class="ranking-table">
      <tbody>
        <tr v-for="(user, index) in users" :key="user.id">
          <td>{{ index + 1 }}</td>
          <td>{{ user.nickname }}</td>
          <td>{{ user.lovepoint }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const users = ref([]);

async function fetchUserRanking() {
  try {
    const response = await axios.get('http://127.0.0.1:8000/user_ranking/');
    users.value = response.data;
  } catch (error) {
    console.error('Error fetching user ranking:', error);
  }
}

onMounted(() => {
  fetchUserRanking();
});
</script>

<style scoped>
.user-ranking {
  max-width: 800px;
  /* 전체적으로 크기를 키웁니다 */
  margin: 0 auto;
}

.ranking-table {
  width: 100%;
  border-collapse: collapse;
}

.ranking-table td {
  padding: 12px;
  /* 셀 내부 여백을 늘립니다 */
  text-align: left;
}

.ranking-table tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.ranking-table tbody {
  background-color: #f2f2f2;
}
</style>
