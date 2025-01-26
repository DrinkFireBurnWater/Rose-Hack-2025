module.exports = {
    darkMode: 'class',
    content: [
      "./src/**/*.{html,js}",
      "./index.html"
    ],
    theme: {
      extend: {
        colors: {
          dark: {
            background: '#1a202c',
            text: '#e2e8f0'
          }
        }
      }
    },
    variants: {
      extend: {
        backgroundColor: ['dark'],
        textColor: ['dark'],
        borderColor: ['dark']
      }
    },
    plugins: []
  }