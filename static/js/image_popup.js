document.addEventListener("DOMContentLoaded", function () {
  const lightbox = document.getElementById("galleryLightbox");
  const lightboxImg = document.getElementById("lightboxImg");
  const lightboxCaption = document.getElementById("lightboxCaption");
  const closeBtn = document.querySelector(".close-lightbox");
  const triggers = document.querySelectorAll(".lightbox-trigger");

  // 1. Listen for clicks on the gallery thumbnails
  triggers.forEach((trigger) => {
    trigger.addEventListener("click", function (event) {
      event.preventDefault(); // Stops the page from jumping or loading a new URL

      const bigImageSrc = this.getAttribute("href");
      const captionText = this.getAttribute("data-caption");

      // Set the popup image source and text
      lightboxImg.src = bigImageSrc;
      lightboxCaption.textContent = captionText;

      // Show the popup by adding the active CSS class
      lightbox.classList.add("active");
    });
  });

  // 2. Close popup when clicking the 'X' button
  closeBtn.addEventListener("click", function () {
    lightbox.classList.remove("active");
  });

  // 3. Close popup when clicking anywhere on the dark background
  lightbox.addEventListener("click", function (event) {
    if (event.target === lightbox) {
      lightbox.classList.remove("active");
    }
  });
});
