<template>
  <Navbar />
  <div class="p-8 max-w-4xl mx-auto">
    <!-- Header -->
    <h1 class="text-3xl font-bold mb-6">Lessons 🚀</h1>

    <!-- Progress Bar -->
    <div class="mb-8">
      <h2 class="text-xl font-semibold mb-2">Your Progress 📊</h2>
      <div class="relative w-full h-6 bg-gray-200 rounded-full overflow-hidden shadow">
        <div
          class="h-full bg-green-500 flex items-center justify-center text-white font-bold"
          :style="{ width: progressPercentage + '%' }"
        >
          {{ progressPercentage }}%
        </div>
      </div>
      <p class="mt-2 text-gray-600">
        {{ progress.lessons_completed }} of {{ progress.total_lessons }} lessons completed 🎯
      </p>
    </div>

    <!-- Lessons List -->
    <div v-if="lessons.length">
      <ul class="space-y-4">
        <li
          v-for="lesson in lessons"
          :key="lesson.id"
          class="border p-4 rounded shadow"
          :class="{ 'bg-green-50 border-green-500': isLessonCompleted(lesson.id) }"
        >
          <!-- Lesson Title -->
          <h2 class="text-xl font-bold flex items-center">
            📚 {{ lesson.title }}
            <span v-if="isLessonCompleted(lesson.id)" class="ml-2 text-green-500">✅</span>
          </h2>

          <!-- Lesson Content -->
          <p class="mt-2">{{ lesson.content }}</p>

          <!-- Video Player -->
          <div v-if="lesson.video_url" class="mt-4">
            <h3 class="text-lg font-semibold mb-2">🎥 Watch Video:</h3>
            <iframe
              :src="formatVideoURL(lesson.video_url)"
              class="w-full h-64 rounded"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
            ></iframe>
          </div>

          <!-- Lesson Completion Button -->
          <button
            v-if="!isLessonCompleted(lesson.id)"
            @click="markLessonComplete(lesson.id)"
            class="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
          >
            ✅ Mark as Complete
          </button>
          <button
            v-else
            class="mt-4 bg-gray-300 text-gray-700 px-4 py-2 rounded cursor-not-allowed"
            disabled
          >
            🎉 Completed!
          </button>
        </li>
      </ul>
    </div>
    <p v-else class="text-gray-500">No lessons available yet. 🚧</p>
  </div>
</template>


<script>
import Navbar from "../components/Navbar.vue";
import axios from "axios";

export default {
  components: { Navbar },
  data() {
    return {
      lessons: [],
      progress: {
        lessons_completed: 0,
        total_lessons: 0,
      },
      courseId: null,
    };
  },
  mounted() {
    this.courseId = localStorage.getItem("current_course_id");
    if (!this.courseId) {
      alert("No course selected. Redirecting to courses.");
      this.$router.push({ name: "Courses" });
    } else {
      this.fetchLessons(this.courseId);
      this.fetchProgress(this.courseId);
    }
  },
  computed: {
    progressPercentage() {
      const completed = this.progress.lessons_completed || 0;
      const total = this.progress.total_lessons || 1;
      return Math.round((completed / total) * 100);
    },
  },
  methods: {
    fetchLessons(courseId) {
      axios
        .get(`http://localhost:8000/api/lessons/?course_id=${courseId}`)
        .then((res) => (this.lessons = res.data.results || []))
        .catch((err) => console.error("Failed to load lessons:", err));
    },
    fetchProgress(courseId) {
      axios
        .get(`http://localhost:8000/api/progress/?course_id=${courseId}`)
        .then((res) => {
          if (res.data.results && res.data.results.length > 0) {
            this.progress = res.data.results[0];
          }
        })
        .catch((err) => console.error("Failed to load progress:", err));
    },
    markLessonComplete(lessonId) {
      axios
        .post(`http://localhost:8000/api/lessons/${lessonId}/complete/`, {
          course_id: this.courseId,
          lesson_id: lessonId,
        })
        .then(() => {
          alert(`Lesson ${lessonId} marked as complete! 🎉`);
          this.fetchProgress(this.courseId);
        })
        .catch((err) => {
          console.error("Failed to mark lesson as complete:", err);
          alert("Failed to mark lesson as complete. 😞");
        });
    },
    isLessonCompleted(lessonId) {
      return this.progress.completed_lessons?.includes(lessonId);
    },
    formatVideoURL(url) {
      try {
        if (url.includes("youtube.com") || url.includes("youtu.be")) {
          const videoId = url.split("v=")[1]?.split("&")[0] || url.split("/").pop();
          return `https://www.youtube.com/embed/${videoId}`;
        }
        return url;
      } catch (e) {
        console.error("Invalid video URL:", url);
        return "";
      }
    },
  },
};
</script>
