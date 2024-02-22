from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import string
import random

app = Flask(__name__)
Bootstrap(app)

url_mapping = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
