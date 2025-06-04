# app.py
from flask import Flask, render_template
from flask_frozen import Freezer
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure Flask to look for templates and static files correctly
app.template_folder = 'templates'
app.static_folder = 'static'  # Assuming you'll add a static folder later for CSS/JS

# Configure Flask-Frozen
# The 'build' folder is the default output directory for Flask-Frozen
# This is where your static HTML files will be generated.
app.config['FREEZER_DESTINATION'] = 'build'
# This tells Flask-Frozen to generate a sitemap.xml
#app.config['FREEZER_SITEMAP_FILENAME'] = 'sitemap.xml'
# IMPORTANT: Setting this to True (or omitting it as it's the default)
# will make Flask-Frozen generate clean URLs like /gallery/index.html
# instead of /gallery.html or just /gallery. This is the standard for static sites.
#app.config['FREEZER_REMOVE_EXTENSIONS'] = True  # <--- CHANGED THIS LINE
freezer = Freezer(app)


# Define a route for the home page ('/')
@app.route('/')
def home():
    # Render the 'index.html' template when the home page is accessed
    return render_template('index.html')


# Define a route for the gallery page ('/gallery')
@app.route('/gallery/')
def gallery():
    # Define the path to your gallery images folder
    gallery_images_dir = os.path.join(app.static_folder, 'images', 'gallery')

    # List to store image filenames
    image_files = []

    # Check if the directory exists to prevent errors
    if os.path.exists(gallery_images_dir):
        # Loop through files in the directory
        for filename in os.listdir(gallery_images_dir):
            # Check if it's a common image file type (you can add more)
            if filename.lower().endswith(
                ('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                # Add the filename to the list
                image_files.append(filename)
        # Sort the image files for consistent order
        image_files.sort()

    # Pass the list of image_files to the gallery.html template
    return render_template('gallery.html', image_files=image_files)


@app.route("/google374d68330201d250.html")
def google_site_verf():
    return render_template("google374d68330201d250.html")


# This block ensures that when app.py is executed directly (e.g., by Netlify's build command),
# it triggers the freezing process to generate static files.
if __name__ == '__main__':
    print(f"Generating static site to: {app.config['FREEZER_DESTINATION']}")
    freezer.freeze()
    print("Static site generation complete.")
