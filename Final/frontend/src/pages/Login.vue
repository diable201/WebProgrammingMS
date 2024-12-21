<template>
  <div class="p-4">
    <Navbar />

    <div class="max-w-sm mx-auto mt-10 bg-white p-6 rounded-lg shadow-lg">
      <h1 class="text-3xl font-bold mb-6 text-center text-blue-600">Welcome Back! 👋</h1>
      <p class="text-center text-gray-600 mb-6">Please sign in to continue.</p>

      <form @submit.prevent="loginUser" class="space-y-4">
        <div>
          <label for="username" class="block text-gray-700 font-medium">Username</label>
          <input
            v-model="username"
            id="username"
            type="text"
            placeholder="Enter your username"
            class="w-full p-3 border rounded focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <div>
          <label for="password" class="block text-gray-700 font-medium">Password</label>
          <input
            v-model="password"
            id="password"
            type="password"
            placeholder="Enter your password"
            class="w-full p-3 border rounded focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-3 rounded hover:bg-blue-700 transition duration-300"
        >
          🚀 Login
        </button>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Navbar from "../components/Navbar.vue";

import axios from "axios";
import { setAuthToken } from "../views/auth";

export default defineComponent({
  name: "Login",
  components: { Navbar },
  setup() {
    const username = ref("");
    const password = ref("");

    function loginUser() {
      axios
        .post("http://localhost:8000/api/auth/token/", {
          username: username.value,
          password: password.value,
        })
        .then((res) => {
          const token = res.data.access;
          setAuthToken(token);

          axios
            .get("http://localhost:8000/api/users/me/", {
              headers: { Authorization: `Bearer ${token}` },
            })
            .then((uRes) => {
              const user = uRes.data;
              localStorage.setItem("is_instructor", user.is_instructor.toString());
              localStorage.setItem("username", user.username);
              localStorage.setItem("user_id", user.id.toString());
              window.location.href = "/";
            })
            .catch(() => alert("Failed to fetch user data"));
        })
        .catch(() => alert("Invalid credentials"));
    }

    return { username, password, loginUser };
  },
});
</script>
