<template>
  <Navbar />
  <div class="p-8">
    <h1 class="text-3xl font-bold mb-4">My Enrollments</h1>
    <ul v-if="enrollments.length" class="space-y-4">
      <li v-for="course in enrollments" :key="course.id" class="border p-4 rounded shadow">
        <h2 class="font-semibold text-lg">{{ course.title }}</h2>
        <p>{{ course.description }}</p>
        <p class="text-sm text-gray-500">Enrolled on: {{ course.enrolled_at }}</p>
      </li>
    </ul>
    <p v-else>No enrolled courses yet.</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import Navbar from '../components/Navbar.vue';
import axios from 'axios';

export default defineComponent({
  name: 'EnrollmentList',
  components: { Navbar },
  setup() {
    const enrollments = ref([]);

    onMounted(() => {
      axios.get('http://localhost:8000/api/enrollments/')
        .then(res => enrollments.value = res.data.results)
        .catch(err => console.error('Failed to load enrollments:', err));
    });

    return { enrollments };
  }
});
</script>
