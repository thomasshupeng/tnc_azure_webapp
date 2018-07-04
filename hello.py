from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    print ("==== root ====")
    return "Hello World!"

if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, ssl_context='adhoc')
    app.run()