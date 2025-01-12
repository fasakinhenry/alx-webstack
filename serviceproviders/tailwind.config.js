/** @type {import('tailwindcss').Config} */
/**
 module.exports = {
  content: [],
  theme: {
    extend: {},
  },
  plugins: [],
}
*/


// filepath: /home/tobijah/alx/alx-webstack/frontend/tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
    '../templates/**/*.html',  // Add this line to include Django templates
    './templates/**/*.html',
    './static/src/**/*.js',
    './app/templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        geist: ['Geist', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
