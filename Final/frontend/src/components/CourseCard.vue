<template>
  <div class="bg-white shadow-lg rounded-lg overflow-hidden hover:shadow-2xl transition duration-300">
    <img
      :src="course.image"
      alt="Course Image"
      class="w-full h-40 object-cover"
      referrerpolicy="no-referrer"
    />
    <div class="p-4">
      <h3 class="font-bold text-xl mb-2">{{ course.title }}</h3>
      <p class="text-gray-700 mb-4">{{ course.description }}</p>
      <p class="text-primary font-semibold">Price: ${{ course.price }}</p>
      <router-link
        :to="{ name: 'CourseDetail', params: { id: course.id } }"
        class="inline-block mt-4 bg-accent text-white py-2 px-4 rounded hover:bg-accent transition"
      >
        View Course
      </router-link>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";
import type {Course} from "../types";

export default defineComponent({
  name: "CourseCard",
  props: {
    course: {
      type: Object as () => Course,
      required: true,
    },

  },
  setup(props) {
    console.log("Image URL for course:", props.course.image);
    return {};
  },
});
</script>
