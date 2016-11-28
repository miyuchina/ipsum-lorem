# External packages
from flask import Flask

# User-defined packages
import dump

static_dir = '/templates'

app = Flask(__name__, static_url_path=static_dir)
dump.generate()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/css/<css_file>')
def css(css_file):
    return app.send_static_file("css/" + css_file)

@app.route('/posts/<year>/<month>/<title>')
def post(year, month, title):
    return app.send_static_file("posts/{}/{}/{}.html".format(year, month, title))

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file("assets/favicon.ico")
