# app.py
from flask import Flask, render_template
from flask_frozen import Freezer
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure Flask to look for templates and static files correctly
app.template_folder = 'templates'
app.static_folder = 'static' # Assuming you'll add a static folder later for CSS/JS

# Configure Flask-Frozen
# The 'build' folder is the default output directory for Flask-Frozen
# This is where your static HTML files will be generated.
app.config['FREEZER_DESTINATION'] = 'build'
freezer = Freezer(app)

# Define a route for the home page ('/')
@app.route('/')
def home():
    # Render the 'index.html' template when the home page is accessed
    return render_template('index.html')

# Define a route for the about page ('/about')
@app.route('/about')
def about():
    # You'll need to create templates/about.html
    return render_template('about.html')

# This block ensures that when app.py is executed directly (e.g., by Netlify's build command),
# it triggers the freezing process to generate static files.
if __name__ == '__main__':
    print(f"Generating static site to: {app.config['FREEZER_DESTINATION']}")
    freezer.freeze()
    print("Static site generation complete.")

