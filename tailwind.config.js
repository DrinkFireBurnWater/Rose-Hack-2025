module.exports = {
    darkMode: 'class',
    content: [
      "./src/**/*.{html,js}",
      "./index.html"
    ],
    theme: {
      extend: {
        // Optional: Add custom dark mode colors if needed
        colors: {
          // Customize dark mode color palette
          dark: {
            background: '#1a202c',
            text: '#e2e8f0'
          }
        }
      }
    },
    variants: {
      extend: {
        // Ensure dark mode variants are enabled for desired classes
        backgroundColor: ['dark'],
        textColor: ['dark'],
        borderColor: ['dark']
      }
    },
    plugins: []
  }