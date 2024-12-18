<template>
  <Navbar />
  <div class="p-8 max-w-4xl mx-auto">
    <!-- User Profile Card -->
    <div class="bg-white shadow-lg rounded-lg p-6 mb-8 border border-gray-200">
      <div class="flex items-center space-x-4">
        <!-- User Avatar -->
        <div class="w-16 h-16 rounded-full bg-blue-500 flex items-center justify-center text-white text-3xl font-semibold">
          {{ user.username.charAt(0).toUpperCase() }}
        </div>
        <!-- User Info -->
        <div>
          <h1 class="text-2xl font-bold text-gray-800">{{ user.username }}'s Profile</h1>
          <p class="text-gray-600 mt-1">Email: <span class="font-medium text-gray-700">{{ user.email }}</span></p>
          <p
            class="mt-2 inline-block px-3 py-1 rounded-full text-white text-sm"
            :class="user.is_instructor ? 'bg-green-500' : 'bg-blue-500'"
          >
            {{ user.is_instructor ? 'Instructor 🎓' : 'Student 📚' }}
          </p>
        </div>
      </div>
    </div>

    <!-- Update Profile Form -->
    <div class="bg-gray-50 p-6 rounded-lg shadow-md border border-gray-200">
      <h2 class="text-xl font-bold text-gray-800 mb-4">Update Your Profile ✏️</h2>
      <form @submit.prevent="updateProfile" class="space-y-4">
        <!-- Email Input -->
        <div>
          <label class="block text-gray-700 font-medium mb-2">New Email</label>
          <input
            v-model="editForm.email"
            type="email"
            class="w-full p-3 border rounded focus:ring-2 focus:ring-blue-500"
            placeholder="Enter your new email"
          />
        </div>

        <!-- Password Input -->
        <div>
          <label class="block text-gray-700 font-medium mb-2">New Password</label>
          <input
            v-model="editForm.password"
            type="password"
            class="w-full p-3 border rounded focus:ring-2 focus:ring-blue-500"
            placeholder="Enter your new password"
          />
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-3 rounded hover:bg-blue-700 transition duration-300"
        >
          Save Changes
        </button>
      </form>
    </div>
  </div>
</template>


<script>
import Navbar from "../components/Navbar.vue";
import axios from "axios";

export default {
  components: { Navbar },
  data() {
    return {
      user: { username: "", email: "", is_instructor: false },
      editForm: { email: "", password: "" },
    };
  },
  mounted() {
    axios.get("http://localhost:8000/api/users/me/").then((res) => {
      this.user = res.data;
      this.editForm.email = this.user.email;
    });
  },
  methods: {
    updateProfile() {
      axios
        .patch("http://localhost:8000/api/users/me/", this.editForm)
        .then(() => {
          alert("Profile updated!");
          this.editForm.password = "";
        })
        .catch((err) => console.error("Failed to update profile:", err));
    },
  },
};
</script>
