npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p  -> Generates the following file, update the file as per the code give below

Update tailwind.config.js

module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

Update postcss.config.js

module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}