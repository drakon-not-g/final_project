from flask import Flask, render_template, redirect, url_for, request, PIL, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index")

if __name__ == "__main__":
    app.run(debug=True)