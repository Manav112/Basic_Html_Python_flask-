from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World ! Basic website using Flask framework , html , python <h1>HEY THERE..ITS ME!<h1>"


@app.route("/<name>")
def user(name):
    return f"Hello There its {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="ADMIN!"))


if __name__ == "__main__":
    app.run()
