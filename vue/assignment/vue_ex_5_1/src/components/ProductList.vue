<template>
  <div>
    <li>
    {{ item.name }} - {{ item.price }}원
  </li>
  </div>
</template>

<script setup>
import {defineProps} from 'vue'
const props = defineProps({
  item:Object
})
</script>

<style scoped>

</style>