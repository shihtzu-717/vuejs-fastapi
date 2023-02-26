import { createApp } from 'vue'
import App from './App.vue'
import VueViewer from 'v-viewer'
// import router from './router'
// import store from './store'
// import 'bootstrap/dist/css/bootstrap.css'
import axios from 'axios'
import '../node_modules/viewerjs/dist/viewer.css'

const app = createApp(App)
app.use(VueViewer)
axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:8000/'// the FastAPI backend
app.mount('#app')
