<template>
  <Navbar />
  <div class="p-8">
    <h1 class="text-2xl font-bold mb-4">Reviews</h1>
    <ul class="space-y-4">
      <li v-for="review in reviews" :key="review.id" class="border p-4 rounded">
        <p><strong>User:</strong> {{ review.user.username }}</p>
        <p>{{ review.comment }}</p>
        <p>Rating: {{ review.rating }}/5</p>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import Navbar from '../components/Navbar.vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

export default defineComponent({
  name: 'ReviewList',
  components: { Navbar },
  setup() {
    const route = useRoute();
    const reviews = ref([]);

    onMounted(() => {
      axios.get(`http://localhost:8000/api/reviews/?course_id=${route.params.id}`)
        .then((res) => (reviews.value = res.data))
        .catch(console.error);
    });

    return { reviews };
  },
});
</script>
