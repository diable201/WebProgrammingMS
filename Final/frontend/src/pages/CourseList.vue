<template>
  <Navbar />
  <div class="p-8">
    <h1 class="text-3xl font-bold mb-4">All Courses</h1>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <CourseCard v-for="course in courses" :key="course.id" :course="course" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import Navbar from '../components/Navbar.vue';
import CourseCard from '../components/CourseCard.vue';
import axios from 'axios';
import type { Course } from '../types';

export default defineComponent({
  name: 'CourseList',
  components: { Navbar, CourseCard },
  setup() {
    const courses = ref<Course[]>([]);

    onMounted(() => {
      axios.get('http://localhost:8000/api/courses/')
        .then((res) => (courses.value = res.data.results))
        .catch(console.error);
    });

    return { courses };
  },
});
</script>
