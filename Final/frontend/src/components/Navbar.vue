<template>
  <nav class="bg-blue-600 text-white p-4 flex justify-between">
    <h1 class="font-bold text-lg">E-Learning</h1>
    <ul class="flex space-x-4">
      <li><router-link to="/">Home</router-link></li>
      <li v-if="isAuthenticated"><router-link to="/profile">Profile</router-link></li>
      <li v-if="isInstructor"><router-link to="/dashboard">Dashboard</router-link></li>
      <li v-if="!isAuthenticated"><router-link to="/login">Login</router-link></li>
      <li v-if="!isAuthenticated"><router-link to="/register">Register</router-link></li>
      <router-link to="/courses" class="text-white hover:underline">Courses</router-link>
      <router-link to="/lessons" class="text-white hover:underline">Lessons</router-link>
      <router-link to="/progress" class="text-white hover:underline">Progress</router-link>
      <li v-if="isAuthenticated">
        <a href="#" @click="logout">Logout</a>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue';

export default defineComponent({
  name: 'Navbar',
  setup() {
    const isAuthenticated = computed(() => !!localStorage.getItem('access_token'));
    const isInstructor = computed(() => localStorage.getItem('is_instructor') === 'true');

    const logout = () => {
      localStorage.clear();
      window.location.href = '/';
    };

    return { isAuthenticated, isInstructor, logout };
  },
});
</script>
