<template>
  <Navbar />
  <div class="p-8 max-w-md mx-auto">
    <h1 class="text-2xl font-bold mb-6">Payment for {{ course.title }}</h1>
    <form @submit.prevent="processPayment" class="space-y-4">
      <input
        v-model="cardNumber"
        type="text"
        placeholder="Card Number"
        class="border p-2 w-full"
        required
      />
      <input
        v-model="cardExpiry"
        type="text"
        placeholder="Expiry Date (MM/YY)"
        class="border p-2 w-full"
        required
      />
      <input
        v-model="cvv"
        type="text"
        placeholder="CVV"
        class="border p-2 w-full"
        required
      />
      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded">
        Pay ${{ course.price }}
      </button>
    </form>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';

export default {
  components: { Navbar },
  data() {
    return {
      course: { title: '', price: '' },
      cardNumber: '',
      cardExpiry: '',
      cvv: '',
    };
  },
  mounted() {
    const route = useRoute();
    const courseId = route.params.id;

    axios.get(`http://localhost:8000/api/courses/${courseId}/`)
      .then(res => this.course = res.data);
  },
  methods: {
    processPayment() {
      axios.post(`http://localhost:8000/api/payments/`, {
        course_id: this.course.id,
        amount: this.course.price,
        card_number: this.cardNumber,
        expiry: this.cardExpiry,
        cvv: this.cvv,
      })
        .then(() => {
          alert('Payment successful! Enrolling in course...');
          this.$router.push({ name: 'CourseDetail', params: { id: this.course.id } });
        })
        .catch(err => console.error('Failed to process payment:', err));
    },
  },
};
</script>
