// Get references to the UI elements
const aboutButton = document.getElementById('about-button');
const homeButton = document.getElementById('home-button');
const dataButton = document.getElementById('data-button');
const articleButtons = document.querySelectorAll('.article-button');
const graphBar = document.getElementById('graph-bar');

// Add event listeners
aboutButton.addEventListener('click', showAboutScreen);
homeButton.addEventListener('click', () => {
  // Stay on the current graphic page
});
dataButton.addEventListener('click', showDataGraph);

articleButtons.forEach((button, index) => {
  button.addEventListener('click', () => {
    // Update the graph bar position and appearance
    graphBar.style.left = `${index * 12.5}%`;
    graphBar.style.width = '12.5%';
    graphBar.style.backgroundColor = getComputedStyle(button).backgroundColor;

    // Add/remove active class from buttons
    articleButtons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');
  });
// Add mouseenter/mouseleave event listeners to highlight the button
  button.addEventListener('mouseenter', () => button.classList.add('hover'));
  button.addEventListener('mouseleave', () => button.classList.remove('hover'));
});

graphBar.addEventListener('mousedown', handleGraphBarDrag);

function showAboutScreen() {
  // Display the about screen
  // ...
}

function showDataGraph() {
  // Navigate to the data graph page
  // ...
}

function handleGraphBarDrag(event) {
  const startX = event.clientX;
  const startLeft = parseInt(graphBar.style.left, 10);

  const mousemove = (moveEvent) => {
    const delta = moveEvent.clientX - startX;
    const newLeft = Math.max(0, Math.min(startLeft + delta, 87.5));
    graphBar.style.left = `${newLeft}%`;
// Update the selected article based on the graph bar position
    const selectedIndex = Math.floor(newLeft / 12.5);
    articleButtons[selectedIndex].click();
  };

  const mouseup = () => {
    document.removeEventListener('mousemove', mousemove);
    document.removeEventListener('mouseup', mouseup);
  };

  document.addEventListener('mousemove', mousemove);
  document.addEventListener('mouseup', mouseup);
}