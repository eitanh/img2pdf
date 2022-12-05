from flask import Flask
from flask import request
from lib.utils import convert
import logging

app = Flask(__name__)

@app.route("/convert")
def hello_world():
    filename = request.args.get('filename')
    return convert(filename)

@app.route("/test")
def test():
   return "Test"

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO,filename="convert.log")
if __name__ == '__main__':
    app.run()