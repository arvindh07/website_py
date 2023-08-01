from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return "<p>Hello, World yes!</p>"


@app.route("/about")
def about():
  return "<h1>About page</h1>"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
