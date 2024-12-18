<template>
  <Navbar />
  <div class="p-8 max-w-3xl mx-auto bg-white shadow-lg rounded-lg border border-gray-200">
    <!-- Quiz Title -->
    <div class="text-center mb-8">
      <h1 class="text-4xl font-extrabold text-blue-700">{{ quiz.title }}</h1>
      <p class="text-gray-500 mt-2">📝 Complete the quiz and test your knowledge!</p>
    </div>

    <!-- Quiz Form -->
    <form @submit.prevent="submitQuiz" class="space-y-8">
      <div
        v-for="(question, index) in questions"
        :key="question.id"
        class="p-6 border-b border-gray-300 last:border-b-0"
      >
        <!-- Question Title -->
        <p class="font-semibold text-lg mb-4">
          <span class="text-blue-600">{{ index + 1 }}.</span> {{ question.question_text }}
        </p>

        <!-- Options -->
        <div class="space-y-3">
          <label
            v-for="option in question.options"
            :key="option.id"
            class="flex items-center space-x-3 cursor-pointer p-2 border rounded-lg hover:bg-gray-50 transition"
            :class="{ 'bg-green-50 border-green-500': answers[question.id] === option.id }"
          >
            <input
              type="radio"
              :name="`question-${question.id}`"
              :value="option.id"
              v-model="answers[question.id]"
              class="h-5 w-5 text-blue-600 focus:ring-blue-500"
            />
            <span class="text-gray-700">{{ option.text }}</span>
          </label>
        </div>
      </div>

      <!-- Submit Button -->
      <div class="text-center">
        <button
          type="submit"
          class="bg-gradient-to-r from-blue-500 to-blue-700 text-white px-6 py-3 rounded-lg shadow hover:from-blue-600 hover:to-blue-800 transition-transform transform hover:scale-105"
        >
          🚀 Submit Quiz
        </button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import Navbar from "../components/Navbar.vue";
import axios from "axios";
import { useRoute } from "vue-router";

export default defineComponent({
  name: "QuizPage",
  components: { Navbar },
  setup() {
    const route = useRoute();
    const quiz = ref({ title: "" });
    const questions = ref([]);
    const answers = ref({});

    onMounted(() => {
      const quizId = route.params.id;

      axios
        .get(`http://localhost:8000/api/quizzes/${quizId}/`)
        .then((res) => (quiz.value = res.data))
        .catch((err) => console.error("Failed to load quiz:", err));

      axios
        .get(`http://localhost:8000/api/quiz-questions/?quiz_id=${quizId}`)
        .then((res) => (questions.value = res.data.results || []))
        .catch((err) => console.error("Failed to load questions:", err));
    });

    function submitQuiz() {
      const quizId = route.params.id;

      axios
        .post(`http://localhost:8000/api/quiz-submission/${quizId}/submit/`, {
          answers: answers.value,
        })
        .then((res) => {
          alert(`🎉 Quiz submitted! Your score: ${res.data.score}`);
        })
        .catch((err) => {
          console.error("Failed to submit quiz:", err);
          alert("Something went wrong. Please try again.");
        });
    }

    return { quiz, questions, answers, submitQuiz };
  },
});
</script>

<style scoped>
.bg-green-50 {
  background-color: #f0fdf4;
}
.border-green-500 {
  border-color: #10b981;
}
</style>
