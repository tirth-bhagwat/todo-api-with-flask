from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    <html>
    <head><title>Todo App Backend</title></head>
    <body><h1>Hello!!</h1></body>
    </html>
    """
