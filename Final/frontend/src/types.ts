export interface User {
  id: number;
  username: string;
  email: string;
  is_student: boolean;
  is_instructor: boolean;
}

export interface Category {
  id: number;
  name: string;
  description: string | null;
}

export interface Course {
  id: number;
  title: string;
  description: string;
  price: number;
  category: Category | null;
  created_at: string;
  instructor: User;
  image: string;
}

export interface Enrollment {
  id: number;
  user_id: number;
  course_id: number;
  enrollment_date: string;
  status: string;
  course?: Course;
}

export interface Lesson {
  id: number;
  course_id: number;
  title: string;
  content: string;
  video_url: string | null;
}

export interface Review {
  id: number;
  course_id: number;
  user: User;
  rating: number;
  comment: string;
  created_at: string;
}

export interface Payment {
  id: number;
  user: number;
  amount: number;
  payment_date: string;
  status: string;
}

export interface QuizQuestion {
  id: number;
  quiz_id: number;
  question_text: string;
  option_a: string;
  option_b: string;
  option_c: string;
  option_d: string;
  correct_option: string;
}

export interface Quiz {
  id: number;
  course_id: number;
  title: string;
  total_marks: number;
  questions: QuizQuestion[];
}

export interface UserProgress {
  id: number;
  user_id: number;
  course_id: number;
  course_title: string;
  lessons_completed: number;
  quiz_scores: Record<string, number>;
  course?: Course;
}
