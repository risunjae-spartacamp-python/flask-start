from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/hiraizumi")
def helloHiraizumi():
    return "hihihihiraizumu"


@app.route("/user/<name>")
def heyName(name):
    return name


# http://127.0.0.1:5000/user/risunjae


@app.route("/user/age/<age>")
def heyAge(age):
    return age


# http://127.0.0.1:5000/user/age/32


@app.route("/user/<name>/<age>")
def heyNameAge(name, age):
    return name + age


@app.route("/html")
def html():
    return "<h1>Hello HTML</h1>"


# http://127.0.0.1:5000/html


# http://127.0.0.1:5000/user/risunjae/32


# http://127.0.0.1:5000/user/age/32


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

# app.run(port=5001)
