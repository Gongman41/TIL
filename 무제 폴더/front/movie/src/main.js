import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import '@/assets/main.css'
import $ from 'jquery';

import App from './App.vue'
import router from './router'

const pinia = createPinia()
const app = createApp(App)

app.config.globalProperties.$ = $;
pinia.use(piniaPluginPersistedstate)
app.use(router)
app.use(pinia)
app.mount('#app')
