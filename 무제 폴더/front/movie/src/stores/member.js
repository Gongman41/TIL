import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMemberStore = defineStore('member', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const profile = ref(null)
  const loginUser = ref(null)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const router = useRouter()

  const signup = function (payload) {
    const { username, password1, password2, nickname, like_genre } = payload
    console.log(like_genre)
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
        nickname,
        like_genre
      }
    })
      .then((response) => {
        const password = password1
        console.log(like_genre)
        login({ username, password })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const login = function (payload) {

    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password
      }
    })
      .then((response) => {
        token.value = response.data.key
        loginUser.value = username
        // console.log(loginUser.value)
        // console.log(token.value)
        // console.log('로그인 성공')
        router.push('/')
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const logout = function () {

    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`
    })
      .then((response) => {
        token.value = null
        loginUser.value = null
        // console.log(loginUser.value)
        // console.log(token.value)
        // console.log('로그아웃 성공')
        router.push('/login')
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const getProfile = function () {
    axios({
      method: 'get',
      url: `${API_URL}/profile/${loginUser.value}`
    })
      .then((response) => {
        profile.value = response.data
      })
      .catch((error) => console.log(error))
  }

  return {
    API_URL, token, isLogin, loginUser, profile,
    signup, login, logout, getProfile
  }
}, { persist: true })
