import { useMemberStore } from '@/stores/member'
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DongjinLoveView from '@/views/DongjinLoveView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'
import UpdateProfile from '@/views/UpdateProfile.vue'
import SearchMoviesView from '@/views/SearchMoviesView.vue'
import MovieWorldCupView from '@/views/MovieWorldCupView.vue'
import test from '@/views/test.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/dongjinlove',
      name: 'DongjinLove',
      component: DongjinLoveView
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
    {
      path: '/moviedetail/:movie_id',
      name: 'MovieDetail',
      component: MovieDetailView
    },
    {
      path: '/profile/:username',
      name: 'Profile',
      component: ProfileView
    },
    {
      path: '/profile/:username/update',
      name: 'UpdateProfile',
      component: UpdateProfile
    },
    {
      path: '/search/:movie_title',
      name: 'SearchMovies',
      component: SearchMoviesView
    },
    {
      path: '/movieworldcup',
      name: 'WorldCup',
      component: MovieWorldCupView
    },
    {
      path: '/test',
      component: test
    },
  ]
})

router.beforeEach((to, from) => {
  const memberStore = useMemberStore()
  if (memberStore.token === null && (to.name !== 'Login' && to.name !== 'SignUp')) {
    return { name: 'Login' }
  }
})

export default router
