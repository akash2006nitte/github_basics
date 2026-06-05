from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    return render_template("home.html")

@app.route("/abc")
def abc():
    return "this is the abc router:"
    return render_template("abc.html")

@app.route("akash")
def abc():
    return "this is the abc router:"
    return render_template("akash.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
