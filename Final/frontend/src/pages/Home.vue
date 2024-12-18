<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Navbar -->
    <Navbar />

    <!-- Hero Section -->
    <section class="bg-primary text-white py-20 text-center">
      <h1 class="text-5xl font-extrabold mb-4">Welcome to E-Learning Platform</h1>
      <p class="text-lg mb-8">Learn from the best courses online, anytime, anywhere.</p>
      <router-link
        to="/courses"
        class="bg-blue-600 text-white py-3 px-6 rounded hover:bg-blue-700 transition duration-300"
      >
        Explore Courses
      </router-link>
    </section>

    <!-- Courses Section -->
    <section class="p-8">
      <h2 class="text-3xl font-bold mb-6 text-center">Available Courses</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <CourseCard
          v-for="course in courses"
          :key="course.id"
          :course="course"
        />
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white text-center py-4">
      <p>&copy; 2024 E-Learning Platform. All rights reserved.</p>
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';
import Navbar from '../components/Navbar.vue';
import CourseCard from '../components/CourseCard.vue';
import axios from 'axios';
import type { Course } from '../types';

export default defineComponent({
  name: 'Home',
  components: { Navbar, CourseCard },
  setup() {
    const courses = ref<Course[]>([]);

    onMounted(() => {
      axios
        .get<Course[]>('http://localhost:8000/api/courses/')
        .then((res) => (courses.value = res.data.results))
        .catch((err) => console.error(err));
    });

    return { courses };
  },
});
</script>
