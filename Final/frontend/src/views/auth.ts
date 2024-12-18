import axios from 'axios';

export function isAuthenticated(): boolean {
  return !!localStorage.getItem("access_token");
}

export function getUserRole(): string | null {
  const user = localStorage.getItem("user");
  if (user) {
    return JSON.parse(user).role; // role: "instructor" or "student"
  }
  return null;
}

export function setAuthToken(token: string | null) {
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    localStorage.setItem('access_token', token);
  } else {
    delete axios.defaults.headers.common['Authorization'];
    localStorage.removeItem('access_token');
  }
}

export function getAuthToken(): string | null {
  return localStorage.getItem('access_token');
}
