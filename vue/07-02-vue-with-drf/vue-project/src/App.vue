<template>
  <header>
    <nav>
      <!-- v-if 붙여서 로그인 여부에 따라 네비게이션 바 변경 -->
      <RouterLink :to="{ name: 'ArticleView'}">Articles</RouterLink>
      <RouterLink :to="{ name: 'SignUpView'}">SiginUpPage</RouterLink>
      <RouterLink :to="{ name: 'LogInView'}">LogInPage</RouterLink>


    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
