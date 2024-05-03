<template>
  <div>
    <p class="'greeting'"> {{msg}}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('Hello')

</script>

<style scoped>
  .greeting {
    color: aqua;
  }
</style>
<!-- 순서는 상관없음 -->
<!-- template 블록은 1개만. script setup도 하나 -->
<!-- scoped가 지정되면 css는 현재 컴포넌트에만 적용됨 -->