<template>
  <div>
    <h1>Article Page</h1>
    <RounterLink :to="{name:'CreateView'}">[CREATE]</RounterLink>
    <ArticleList/>
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
import {onMounted} from 'vue'
import { useCounterStore } from '@/stores/counter'
import {RounterLink} from 'vue-router'
const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})
// 서버가 브라우저에 인증서 제공(CORS떄매)
</script>

<style>

</style>
