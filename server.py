# External packages
from flask import Flask

# User-defined packages
# import dump

app = Flask(__name__)
# dump.generate()

@app.route('/')
def index():
    return app.send_static_file('index.html')
