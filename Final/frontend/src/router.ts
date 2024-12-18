import { createRouter, createWebHistory } from 'vue-router';

import Home from '../src/pages/Home.vue';
import Login from '../src/pages/Login.vue';
import Register from '../src/pages/Register.vue';
import CourseDetail from '../src/pages/CourseDetail.vue';
import CourseList from '../src/pages/CourseList.vue';
import CategoryList from '../src/pages/CategoryList.vue';
import EnrollmentList from '../src/pages/EnrollmentList.vue';
import InstructorDashboard from '../src/pages/InstructorDashboard.vue';
import LessonList from '../src/pages/LessonList.vue';
import PaymentForm from '../src/pages/PaymentForm.vue';
import QuizPage from '../src/pages/QuizPage.vue';
import ReviewList from '../src/pages/ReviewList.vue';
import UserProfile from '../src/pages/UserProfile.vue';
import UserProgress from '../src/pages/UserProgress.vue';
import {getUserRole, isAuthenticated} from "@/views/auth.ts";
import * as path from "node:path";

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/courses', name: 'Courses', component: CourseList },
  { path: '/course/:id', name: 'CourseDetail', component: CourseDetail },
  { path: '/categories', name: 'CategoryList', component: CategoryList },
  { path: '/enrollments', name: 'EnrollmentList', component: EnrollmentList },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: InstructorDashboard,
    meta: { requiresAuth: true, requiresInstructor: true }
  },
  {
    path: "/profile",
    name: "UserProfile",
    component: UserProfile,
    meta: { requiresAuth: true },
  },
  { path: '/lessons', name: 'LessonList', component: LessonList },
  { path: '/payment', name: 'PaymentForm', component: PaymentForm },
  { path: '/quiz/:id', name: 'QuizPage', component: QuizPage },
  { path: '/reviews', name: 'ReviewList', component: ReviewList },
  { path: '/progress', name: 'UserProgress', component: UserProgress },
  { path: '/:pathMatch(.*)*', redirect: '/' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Global Navigation Guard
router.beforeEach((to, from, next) => {
  const requiresAuth = to.meta.requiresAuth;
  const role = to.meta.role;

  if (requiresAuth && !isAuthenticated()) {
    next({ name: "Login" });
  } else if (role && getUserRole() !== role) {
    next({ name: "Home" });
  } else {
    next();
  }
});

export default router;
