import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const isLogin = computed(() => {
    if (token.value ===null) {
      return false
    } else {
      return true
    }
  })

  const signUp = function (payload) {
    //  사용자 입력데이터를 받아 axios로 django에 요청을 보냄
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    const { username,password1,password2} = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data:[username,password1,password2]
    })
    .then((response)=>{
      console.log('회원가입 성공')
      const password = password1
      logIn({username,password})
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const logIn = function(payload) {
    // 사용자 입력데이터를 받아 axios로 django 에 요청을 보내고 성공 후 응답받은 토큰을 저장
    const { username,password} = payload

    axios({
      method:'get',
      url:`${API_URL}/accounts/login/`,
      data: {
        username,password
      }
    })
    .then((response)=>{
      console.log('로그인 성공')
      token.value = response.data.key
      router.push({name:"ArticleView"})
    })
    .catch((error) => {
      console.log(error)
    })
  }
  return { articles, API_URL, getArticles,signUp,logIn,token , isLogin}
}, { persist: true })
