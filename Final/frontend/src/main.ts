import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/tailwind.css';
import axios from "axios";

const token = localStorage.getItem('access_token'); // Replace 'auth_token' with the key you use for storing the token
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  console.log('Token:', token);

}

createApp(App).use(router).mount('#app');
