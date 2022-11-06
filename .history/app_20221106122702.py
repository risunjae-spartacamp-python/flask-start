from flask import Flask
from flask import render_template
from flask import request

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
    # return "<h1>Hello HTML</h1>"
    return render_template("index.html")


@app.route("/html/name/<name>")
def htmlName(name):
    # return "<h1>Hello HTML</h1>"
    return render_template("name.html", name=name)


@app.route("/html/age/<age>")
def htmlAge(age):
    return render_template("age.html", age=age)


@app.route("/query")
def query():
    search_text = request.args.get("search_text")
    print("search_text")
    print
    return search_text


# http://127.0.0.1:5000/query?search_text=AAA

# http://127.0.0.1:5000/html


# http://127.0.0.1:5000/user/risunjae/32


# http://127.0.0.1:5000/user/age/32


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

# app.run(port=5001)
