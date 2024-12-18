<template>
  <div class="p-4 bg-gray-50 min-h-screen">
    <!-- Navbar -->
    <Navbar />

    <!-- Registration Form Card -->
    <div class="max-w-md mx-auto mt-10 bg-white p-6 rounded-lg shadow-lg">
      <h1 class="text-3xl font-bold text-center text-green-600 mb-6">
        Create Your Account 🚀
      </h1>
      <p class="text-center text-gray-500 mb-4">
        Sign up to start your learning journey!
      </p>

      <!-- Registration Form -->
      <form @submit.prevent="registerUser" class="space-y-4">
        <!-- Username Field -->
        <div>
          <label for="username" class="block text-gray-700 font-medium mb-1">
            Username
          </label>
          <input
            v-model="username"
            id="username"
            type="text"
            placeholder="Enter your username"
            class="w-full p-3 border rounded focus:ring-2 focus:ring-green-500"
            required
          />
        </div>

        <!-- Email Field -->
        <div>
          <label for="email" class="block text-gray-700 font-medium mb-1">
            Email
          </label>
          <input
            v-model="email"
            id="email"
            type="email"
            placeholder="Enter your email"
            class="w-full p-3 border rounded focus:ring-2 focus:ring-green-500"
            required
          />
        </div>

        <!-- Password Field -->
        <div>
          <label for="password" class="block text-gray-700 font-medium mb-1">
            Password
          </label>
          <input
            v-model="password"
            id="password"
            type="password"
            placeholder="Enter your password"
            class="w-full p-3 border rounded focus:ring-2 focus:ring-green-500"
            required
          />
        </div>

        <!-- Confirm Password Field -->
        <div>
          <label for="password_confirmation" class="block text-gray-700 font-medium mb-1">
            Confirm Password
          </label>
          <input
            v-model="password_confirmation"
            id="password_confirmation"
            type="password"
            placeholder="Confirm your password"
            class="w-full p-3 border rounded focus:ring-2 focus:ring-green-500"
            required
          />
        </div>

        <!-- Instructor Checkbox -->
        <label class="flex items-center space-x-2 text-gray-700">
          <input
            type="checkbox"
            v-model="is_instructor"
            class="h-5 w-5 text-green-500"
          />
          <span>I am registering as an instructor</span>
        </label>

        <!-- Submit Button -->
        <button
          type="submit"
          class="w-full bg-green-600 text-white py-3 rounded hover:bg-green-700 transition duration-300"
        >
          Register
        </button>
      </form>

      <!-- Redirect to Login -->
      <p class="text-center text-gray-500 mt-4">
        Already have an account?
        <router-link to="/login" class="text-green-600 hover:underline"
          >Log in here</router-link
        >.
      </p>
    </div>
  </div>
</template>


<script lang="ts">
import { defineComponent, ref } from "vue";
import Navbar from "../components/Navbar.vue";
import axios from "axios";

export default defineComponent({
  name: "Register",
  components: { Navbar },
  setup() {
    const username = ref("");
    const email = ref("");
    const password = ref("");
    const password_confirmation = ref("");
    const is_instructor = ref(false);

    const errorMessage = ref("");

    const registerUser = () => {
      if (password.value !== password_confirmation.value) {
        errorMessage.value = "Passwords do not match! 🔐";
        return;
      }

      axios
        .post("http://localhost:8000/api/users/register/", {
          username: username.value,
          email: email.value,
          password: password.value,
          password_confirmation: password_confirmation.value,
          is_instructor: is_instructor.value,
        })
        .then(() => {
          alert("Registration successful! 🎉 Please login to continue.");
          window.location.href = "/login";
        })
        .catch((err) => {
          console.error(err);
          errorMessage.value = err.response?.data?.detail || "Registration failed!";
        });
    };

    return {
      username,
      email,
      password,
      password_confirmation,
      is_instructor,
      registerUser,
      errorMessage,
    };
  },
});
</script>
