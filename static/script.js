document.addEventListener('DOMContentLoaded', () => {
    const galleryImageLinks = document.querySelectorAll('.gallery-image-link');
    const lightboxModal = document.getElementById('lightbox-modal');
    const lightboxImage = document.querySelector('.lightbox-image');
    const lightboxCaption = document.querySelector('.lightbox-caption');
    const lightboxClose = document.querySelector('.lightbox-close');

    // Function to open the lightbox
    const openLightbox = (imageUrl, captionText) => {
        lightboxImage.src = imageUrl;
        lightboxImage.alt = captionText; // Set alt text for accessibility
        lightboxCaption.textContent = captionText;
        lightboxModal.style.display = 'flex'; // Make it visible (using flex for centering)
    };

    // Function to close the lightbox
    const closeLightbox = () => {
        lightboxModal.style.display = 'none'; // Hide it
        lightboxImage.src = ''; // Clear image source
        lightboxImage.alt = ''; // Clear alt text
        lightboxCaption.textContent = ''; // Clear caption
    };

    // Add click event listeners to all image links in the gallery
    galleryImageLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent the default link behavior (opening in new tab)
            const largeSrc = link.getAttribute('data-large-src');
            // Get caption from data-alt or fallback to item-caption text
            const caption = link.getAttribute('data-alt') || link.querySelector('.item-caption')?.textContent;
            openLightbox(largeSrc, caption);
        });
    });

    // Add click event listener to the close button
    lightboxClose.addEventListener('click', closeLightbox);

    // Close the lightbox if clicked outside the image content
    lightboxModal.addEventListener('click', (event) => {
        if (event.target === lightboxModal) { // Only close if the click is directly on the modal background
            closeLightbox();
        }
    });

    // Optional: Close with Escape key
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && lightboxModal.style.display === 'flex') {
            closeLightbox();
        }
    });
});
