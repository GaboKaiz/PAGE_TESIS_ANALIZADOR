/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#1e3a8a", // Azul oscuro
        secondary: "#4b5563", // Gris oscuro
        accent: "#f59e0b", // Amarillo
        background: "#f3f4f6", // Gris claro
        error: "#dc2626", // Rojo
        success: "#15803d", // Verde
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
      },
    },
  },
  plugins: [],
};
