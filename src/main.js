import './assets/main.css'

import Button from './components/Button.vue'


import { createApp, VueElement } from 'vue'
import App from './App.vue'
const app = createApp(App)

app.component('MyButton',Button)
app.mount('#app')
