/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'restaurante-principal': '#f87171', // Un rojo suave para tu marca
      }
    },
  },
  plugins: [],
}