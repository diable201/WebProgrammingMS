/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1877F2',
        secondary: '#F0F2F5',
        dark: '#242526',
        light: '#FFFFFF',
        accent: '#1E90FF',
        footer: '#18191A',
      },
    },
  },
  plugins: [],
};
