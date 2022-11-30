from flask import Flask
from flask import request
from lib.utils import convert
app = Flask(__name__)

@app.route("/convert")
def hello_world():
    filename = request.args.get('filename')
    return convert(filename)

if __name__ == '__main__':
    app.run()