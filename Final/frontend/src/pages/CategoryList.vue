<template>
  <div class="p-4">
    <Navbar/>
    <div class="max-w-3xl mx-auto mt-8">
      <h1 class="text-2xl font-bold mb-4">Categories</h1>
      <div v-for="cat in categories" :key="cat.id" class="mb-8">
        <h2 class="text-xl font-semibold">{{ cat.name }}</h2>
        <p class="text-sm text-gray-600">{{ cat.description }}</p>
        <ul class="mt-2 space-y-2 ml-4">
          <li v-for="course in courses.filter(c=>c.category && c.category.id===cat.id)" :key="course.id">
            <router-link :to="{name:'course-detail', params:{id:course.id}}" class="text-blue-600 underline">{{ course.title }}</router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import Navbar from '../components/Navbar.vue'
import axios from 'axios'
import type { Category, Course } from '../types'

export default defineComponent({
  name:'CategoryList',
  components:{Navbar},
  setup(){
    const categories = ref<Category[]>([])
    const courses = ref<Course[]>([])

    onMounted(()=>{
      axios.get<Category[]>('http://localhost:8000/api/categories/')
        .then(res=> categories.value=res.data)
        .catch(err=>console.error(err));
      axios.get<Course[]>('http://localhost:8000/api/courses/')
        .then(res=>courses.value=res.data)
        .catch(err=>console.error(err));
    })

    return {categories,courses}
  }
})
</script>
