from flask import Flask

app = Flask("myapp")

@app.route("/")
def home():
    return "<h1>Hello world</h1>"


@app.route("/about")
def about():
    return "About page!"


app.run()

