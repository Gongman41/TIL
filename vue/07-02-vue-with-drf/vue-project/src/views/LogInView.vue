<template>
  <div>
    <h1>LogInPage</h1>
    <form @submit.prevent="logIn">
      <div>
        <label for="username">username : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password">password : </label>
        <input type = "password" v-model.trim="password1" id="password">
      </div>

      <input type="submit">
    </form>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useCounterStore} from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password = ref(null)

const logIn = function() {
  const payload = {
    username:username.value,
    password:password.value
  }
  store.logIn(payload)
}
</script>

<style>

</style>
