document.getElementById('animehub').addEventListener('click', function() {
  var overlay = document.getElementById('animationOverlay');
  overlay.style.display = 'flex'; // Show the overlay
  
  // Optional: Hide the overlay after the GIF animation completes (e.g., after 5 seconds)
  setTimeout(function() {
    overlay.style.display = 'none'; // Hide the overlay
  }, 5000); // Adjust this time based on the GIF duration
});
