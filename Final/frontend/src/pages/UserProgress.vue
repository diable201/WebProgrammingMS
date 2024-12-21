<template>
  <Navbar/>
  <div class="p-8 max-w-4xl mx-auto">
    <!-- Header -->
    <h1 class="text-3xl font-bold mb-6">Your Progress 📊</h1>

    <!-- Progress Cards -->
    <div v-if="progress.length">
      <div
        v-for="item in progress"
        :key="item.id"
        class="p-6 border rounded-lg mb-6 shadow-lg bg-white"
      >
        <!-- Course Title -->
        <h2 class="font-bold text-xl text-blue-600 mb-4 flex items-center">
          📚 {{ item.course_title || 'Course Title Not Available' }}
        </h2>

        <!-- Lessons Progress -->
        <div class="mb-4">
          <p class="font-medium mb-2">Lessons Progress 🎯</p>
          <div class="relative w-full h-6 bg-gray-200 rounded-full overflow-hidden">
            <div
              class="h-full bg-green-500 flex items-center justify-center text-white text-sm font-bold"
              :style="{ width: getProgressPercentage(item.lessons_completed, item.total_lessons) + '%' }"
            >
              {{ getProgressPercentage(item.lessons_completed, item.total_lessons) }}%
            </div>
          </div>
          <p class="mt-2 text-gray-600">
            {{ item.lessons_completed || 0 }} of {{ item.total_lessons || 0 }} lessons completed ✅
          </p>
        </div>

        <!-- Quizzes Progress -->
        <div class="mb-4">
          <p class="font-medium mb-2">Quizzes Progress 📝</p>
          <div class="relative w-full h-6 bg-gray-200 rounded-full overflow-hidden">
            <div
              class="h-full bg-yellow-500 flex items-center justify-center text-white text-sm font-bold"
              :style="{ width: getProgressPercentage(item.quizzes_completed, item.total_quizzes) + '%' }"
            >
              {{ getProgressPercentage(item.quizzes_completed, item.total_quizzes) }}%
            </div>
          </div>
          <p class="mt-2 text-gray-600">
            {{ item.quizzes_completed || 0 }} of {{ item.total_quizzes || 0 }} quizzes completed 🏆
          </p>
        </div>
      </div>
    </div>

    <!-- No Progress Data -->
    <p v-else class="text-gray-500 text-lg text-center">
      😞 No progress data available. Start a course now!
    </p>
  </div>
</template>


<script>
import Navbar from "../components/Navbar.vue";
import axios from "axios";

export default {
  components: {Navbar},
  data() {
    return {
      progress: [],
    };
  },
  mounted() {
    this.fetchProgress();
  },
  methods: {
    fetchProgress() {
      axios
        .get("http://localhost:8000/api/progress/")
        .then((res) => {
          if (res.data.results) {
            this.progress = res.data.results;
          } else {
            this.progress = [];
          }
        })
        .catch((err) => {
          console.error("Failed to load progress:", err);
          this.progress = [];
        });
    },
    getProgressPercentage(completed, total) {
      if (!total || total === 0) return 0;
      return Math.round((completed / total) * 100);
    },
  },
};
</script>
