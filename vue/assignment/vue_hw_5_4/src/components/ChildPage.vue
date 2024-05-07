<template>
  <div>
    <h3>자식페이지입니다.</h3>
    <p>이름: {{ props.name }}</p>
    <p>나이: {{ props.age }}</p>
    <p>용돈: {{ props.balance }}</p>
    <button @click="updateBalance">용돈 올려주세요</button>

  </div>
</template>

<script setup> 
import { defineProps,defineEmits } from 'vue'

const props = defineProps({
  name: String,
  age: Number,
  balance: Number
})

const emit = defineEmits([
  'updateBalance'
])

const updateBalance = function() {
  emit('updateBalance')
}
</script>
<style>
</style>