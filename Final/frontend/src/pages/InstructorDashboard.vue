<template>
  <Navbar />
  <div class="p-8 max-w-6xl mx-auto">
    <!-- Instructor Dashboard Title -->
    <h1 class="text-3xl font-bold mb-8 text-gray-800 text-center">
      👨‍🏫 Instructor Dashboard
    </h1>

    <!-- My Courses Section -->
    <section>
      <h2 class="text-2xl font-semibold mb-6 text-gray-700">📚 My Courses</h2>
      <div v-if="courses.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="course in courses"
          :key="course.id"
          class="border border-gray-200 rounded-lg shadow-md p-4 hover:shadow-lg transition duration-300 bg-white"
        >
          <h3 class="font-bold text-lg text-blue-600">{{ course.title }}</h3>
          <p class="text-gray-600 mt-2 line-clamp-3">{{ course.description }}</p>
          <p class="mt-3 text-sm text-gray-700">
            💰 <span class="font-medium">Price:</span> ${{ course.price }}
          </p>
          <p class="text-sm text-gray-500 mt-1">📅 Created on: {{ formatDate(course.created_at) }}</p>
        </div>
      </div>
      <p v-else class="text-gray-500 mt-4">No courses found. Start by creating a course below.</p>
    </section>

    <!-- Divider -->
    <hr class="my-10 border-t-2 border-gray-200" />

    <!-- Create Course Section -->
    <section class="mt-8">
      <h2 class="text-2xl font-semibold mb-4 text-gray-700">🆕 Create New Course</h2>
      <div class="bg-gray-50 p-6 rounded-lg shadow-md border border-gray-200">
        <form @submit.prevent="createCourse" class="space-y-4">
          <!-- Course Title -->
          <div>
            <label class="block font-medium text-gray-700 mb-1">Course Title</label>
            <input
              v-model="form.title"
              type="text"
              class="w-full p-3 border rounded focus:ring-2 focus:ring-blue-500"
              placeholder="Enter course title"
              required
            />
          </div>

          <!-- Course Description -->
          <div>
            <label class="block font-medium text-gray-700 mb-1">Course Description</label>
            <textarea
              v-model="form.description"
              rows="4"
              class="w-full p-3 border rounded focus:ring-2 focus:ring-blue-500"
              placeholder="Enter course description"
              required
            ></textarea>
          </div>

          <!-- Course Price -->
          <div>
            <label class="block font-medium text-gray-700 mb-1">Course Price ($)</label>
            <input
              v-model="form.price"
              type="number"
              step="0.01"
              class="w-full p-3 border rounded focus:ring-2 focus:ring-blue-500"
              placeholder="Enter price"
              required
            />
          </div>

          <!-- Select Category -->
          <div>
            <label class="block font-medium text-gray-700 mb-1">Select Category</label>
            <select
              v-model="form.category_id"
              class="w-full p-3 border rounded focus:ring-2 focus:ring-blue-500"
              required
            >
              <option disabled value="">Select a category</option>
              <option v-for="category in categories" :key="category.id" :value="category.id">
                {{ category.name }}
              </option>
            </select>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            class="w-full bg-blue-600 text-white py-3 rounded hover:bg-blue-700 transition duration-300"
          >
            🚀 Create Course
          </button>
        </form>
      </div>
    </section>
  </div>
</template>


<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import Navbar from "../components/Navbar.vue";
import axios from "axios";
import { getAuthToken, setAuthToken } from "@/views/auth";

export default defineComponent({
  name: "InstructorDashboard",
  components: { Navbar },
  setup() {
    const courses = ref([]);
    const categories = ref([]);
    const form = ref({
      title: "",
      description: "",
      price: "",
      category_id: "",
    });

    const fetchData = () => {
      const token = getAuthToken();
      const instructor_id = localStorage.getItem("user_id");

      if (!token || !instructor_id) {
        alert("You are not logged in as an instructor!");
        window.location.href = "/login";
        return;
      }
      setAuthToken(token);
      axios
        .get("http://localhost:8000/api/courses/")
        .then((res) => {
          courses.value = res.data.results
        })
        .catch((err) => console.error("Failed to load courses:", err));

      axios
        .get("http://localhost:8000/api/categories/")
        .then((res) => {
          categories.value = res.data.results;
        })
        .catch((err) => console.error("Failed to load categories:", err));
    };

    const createCourse = () => {
      const instructor_id = localStorage.getItem("user_id");
      if (!instructor_id) {
        alert("Instructor ID missing. Please log in.");
        return;
      }

      const newCourse = {
        ...form.value,
        instructor_id: +instructor_id,
      };

      axios
        .post("http://localhost:8000/api/courses/", newCourse)
        .then(() => {
          alert("Course created successfully!");
          fetchData();
          resetForm();
        })
        .catch((err) => {
          console.error("Failed to create course:", err);
          alert(err.response?.data?.detail || "An error occurred.");
        });
    };

    const resetForm = () => {
      form.value = { title: "", description: "", price: "", category_id: "" };
    };

    const formatDate = (dateString: string) => {
      return new Date(dateString).toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    };

    onMounted(fetchData);

    return {
      courses,
      categories,
      form,
      createCourse,
      formatDate,
    };
  },
});
</script>
