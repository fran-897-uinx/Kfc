    // theme/tailwind.config.js
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: [
        './templates/**/*.html',
        './**/templates/**/*.html',
        './theme/static/src/**/*.js', // If you have custom JS for DaisyUI components
      ],
      theme: {
        extend: {},
      },
      plugins: [require('daisyui')],
      // DaisyUI configuration (optional)
      daisyui: {
        themes: ["light", "dark", "cupcake"], // Add desired themes
      },
    };