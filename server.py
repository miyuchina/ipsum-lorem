# External packages
from flask import Flask

# User-defined packages
# import dump

app = Flask(__name__)
# dump.generate()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/css/<css_file>')
def css(css_file):
    return app.send_static_file("css/" + css_file)

@app.route('/posts/<post_name>')
def post(post_name):
    return app.send_static_file("posts/" + post_name)
