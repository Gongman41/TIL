<template>
  <div>
    <h3>자식페이지입니다.</h3>
    <p>이름: {{ props.name }}</p>
    <p>나이: {{ props.age }}</p>
  </div>
</template>

<script setup> 
import { defineProps } from 'vue'

const props = defineProps({
  name: String,
  age: Number
})
</script>
<style>
</style>