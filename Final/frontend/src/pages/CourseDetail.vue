<template>
  <Navbar/>
  <div class="p-8 max-w-6xl mx-auto">
    <!-- Course Hero Section -->
    <div class="bg-gradient-to-r from-blue-500 to-indigo-500 text-white p-8 rounded-lg shadow-lg mb-8">
      <h1 class="text-4xl font-extrabold">{{ course.title || "Course Title" }}</h1>
      <p class="text-lg mt-2">{{ course.description || "Course description goes here." }}</p>
      <p class="text-2xl font-semibold mt-4">💰 Price: ${{ course.price || "0.00" }}</p>
    </div>

    <!-- Payment Form Section -->
    <div v-if="!isPaid" class="bg-white p-6 shadow-lg rounded-lg mb-6">
      <h2 class="text-2xl font-bold text-gray-800 mb-4">Payment Required 💳</h2>
      <form @submit.prevent="processPayment" class="space-y-4">
        <input
          v-model="cardNumber"
          type="text"
          placeholder="Card Number"
          class="border p-3 w-full rounded focus:ring-2 focus:ring-blue-500"
          required
        />
        <input
          v-model="cardExpiry"
          type="text"
          placeholder="Expiry Date (MM/YY)"
          class="border p-3 w-full rounded focus:ring-2 focus:ring-blue-500"
          required
        />
        <input
          v-model="cvv"
          type="text"
          placeholder="CVV"
          class="border p-3 w-full rounded focus:ring-2 focus:ring-blue-500"
          required
        />
        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition duration-300"
        >
          Pay & Enroll 🚀
        </button>
      </form>
    </div>

    <!-- Enrollment Confirmation -->
    <p v-else-if="!isEnrolled" class="text-green-600 text-lg text-center mt-4">
      ⏳ Processing Enrollment...
    </p>

    <!-- Course Content -->
    <div v-if="isEnrolled" class="space-y-12">
      <!-- Lessons Section -->
      <section>
        <h2 class="text-3xl font-bold text-blue-600 mb-4">📚 Lessons</h2>
        <div v-if="lessons.length" class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div
            v-for="lesson in lessons"
            :key="lesson.id"
            class="bg-white p-6 rounded-lg shadow-lg hover:shadow-2xl transition-shadow duration-300"
          >
            <h3 class="text-xl font-semibold text-gray-800">{{ lesson.title }}</h3>
            <p class="text-gray-600 mt-2">{{ lesson.content }}</p>
            <div v-if="lesson.video_url" class="mt-4 rounded-lg overflow-hidden">
              <iframe
                width="100%"
                height="200"
                :src="embedYouTubeURL(lesson.video_url)"
                class="rounded-lg"
                frameborder="0"
                allow="autoplay; encrypted-media; picture-in-picture"
                allowfullscreen
              ></iframe>
            </div>
          </div>
        </div>
        <p v-else class="text-gray-500">No lessons available.</p>
      </section>

      <!-- Reviews Section -->
      <section>
        <h2 class="text-3xl font-bold text-yellow-500 mb-4">⭐ Reviews</h2>
        <div v-if="reviews.length" class="space-y-4">
          <div
            v-for="review in reviews"
            :key="review.id"
            class="bg-yellow-50 p-4 border-l-4 border-yellow-500 rounded-lg shadow-md"
          >
            <p class="font-semibold text-yellow-600">⭐ {{ review.rating }}/5</p>
            <p class="text-gray-600 mt-1 italic">{{ review.comment }}</p>
          </div>
        </div>
        <p v-else class="text-gray-500">No reviews yet.</p>

        <!-- Add Review Form -->
        <h3 class="text-2xl font-semibold text-gray-700 mt-6">Write a Review ✍️</h3>
        <div class="flex items-center space-x-2 mb-4">
          <span
            v-for="n in 5"
            :key="n"
            @click="setRating(n)"
            class="cursor-pointer text-3xl"
            :class="n <= rating ? 'text-yellow-500' : 'text-gray-300'"
          >
            ★
          </span>
        </div>
        <form @submit.prevent="submitReview" class="space-y-4">
          <textarea
            v-model="reviewText"
            placeholder="Share your thoughts..."
            class="w-full border p-3 rounded focus:ring-2 focus:ring-yellow-500"
          ></textarea>
          <button
            type="submit"
            class="bg-yellow-500 text-white py-2 px-4 rounded hover:bg-yellow-600 transition duration-300"
          >
            Submit Review 🚀
          </button>
        </form>
      </section>

      <!-- Quizzes Section -->
      <section>
        <h2 class="text-3xl font-bold text-purple-600 mb-4">📝 Quizzes</h2>
        <div class="text-center">
          <button
            v-if="quiz"
            @click="startQuiz"
            class="bg-purple-600 text-white py-3 px-6 rounded-lg hover:bg-purple-700 transition duration-300"
          >
            Start Quiz ➡️
          </button>
          <p v-else class="text-gray-500">No quizzes available.</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import axios from "axios";
import {useRoute} from "vue-router";

export default {
  components: {Navbar},
  data() {
    return {
      course: {},
      lessons: [],
      reviews: [],
      quiz: null,
      isPaid: false,
      isEnrolled: false,
      cardNumber: "",
      cardExpiry: "",
      cvv: "",
      reviewText: "",
      rating: 0,
    };
  },
  mounted() {
    const route = useRoute();
    const courseId = route.params.id;

    this.attachToken();
    this.fetchCourseDetails(courseId);
    this.checkEnrollment(courseId);
    this.fetchReviews(courseId);
  },
  methods: {
    attachToken() {
      axios.interceptors.request.use((config) => {
        const token = localStorage.getItem("token");
        if (token) config.headers["Authorization"] = `Bearer ${token}`;
        return config;
      });
    },
    fetchCourseDetails(courseId) {
      axios.get(`http://localhost:8000/api/courses/${courseId}/`).then((res) => (this.course = res.data));
    },
    checkEnrollment(courseId) {
      const userId = localStorage.getItem("user_id");
      axios.get(`http://localhost:8000/api/enrollments/?user_id=${userId}&course_id=${courseId}`).then((res) => {
        if (res.data.results?.length > 0) {
          this.isEnrolled = true;
          this.isPaid = true;
          this.fetchLessonsAndQuiz(courseId);
        }
      });
    },
    fetchReviews(courseId) {
      axios.get(`http://localhost:8000/api/reviews/?course_id=${courseId}`).then((res) => (this.reviews = res.data.results));
    },
    fetchLessonsAndQuiz(courseId) {
      axios.get(`http://localhost:8000/api/lessons/?course_id=${courseId}`).then((res) => (this.lessons = res.data.results));
      axios.get(`http://localhost:8000/api/quizzes/?course_id=${courseId}`).then((res) => (this.quiz = res.data.results[0]));
    },
    processPayment() {
      axios.post("http://localhost:8000/api/payments/", {
        course_id: this.course.id,
        amount: this.course.price,
        card_number: this.cardNumber,
        expiry: this.cardExpiry,
        cvv: this.cvv,
      })
        .then(() => {
          alert("Payment successful!");
          this.isPaid = true;
          this.enrollInCourse(this.course.id);
        })
        .catch((err) => {
          console.error("Payment failed:", err);
          alert("Payment failed. Please try again.");
        });
    },
    enrollInCourse(courseId) {
      const userId = localStorage.getItem("user_id");
      axios.post("http://localhost:8000/api/enrollments/", {
        course_id: courseId,
        user_id: userId,
      })
        .then(() => {
          this.isEnrolled = true;
          localStorage.setItem('current_course_id', courseId);
          this.fetchLessonsAndQuiz(courseId);
        })
        .catch((err) => {
          console.error("Enrollment failed:", err);
          alert("Enrollment failed. Please contact support.");
        });
    },
    submitReview() {
      axios.post("http://localhost:8000/api/reviews/", {
        course_id: this.course.id,
        rating: this.rating,
        comment: this.reviewText
      }).then(() => {
        alert("Review submitted!");
        this.reviewText = "";
        this.fetchReviews(this.course.id);
      });
    },
    setRating(n) {
      this.rating = n;
    },
    embedYouTubeURL(url) {
      const videoId = url.split("v=")[1]?.split("&")[0];
      return `https://www.youtube.com/embed/${videoId}`;
    },
    startQuiz() {
      this.$router.push({name: "QuizPage", params: {id: this.quiz.id}});
    },
  },
};
</script>
