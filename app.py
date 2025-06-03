# app.py
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

"""
unquote if workaround below doesn't work
# Define a route for the home page ('/')
@app.route('/')
def home():
    # Render the 'index.html' template when the home page is accessed
    return render_template('index.html')

# This block ensures the Flask development server runs only when the script is executed directly
if __name__ == '__main__':
    # Run the Flask application in debug mode (useful for development, automatically reloads on code changes)
    app.run(debug=True)
"""

"""
@app.route('/')
def home():
    return 'Hello, Replit!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

"""

# after frozen-flask

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    freezer.freeze()

