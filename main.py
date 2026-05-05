from flask import Flask, render_template, redirect, url_for, request, session
from PIL import Image, ImageDraw, ImageFont
import database
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/creater")
def creater():
    return render_template("creater.html")

@app.route("/gareley")
def gareley():
    return render_template("gareley.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        login = request.form["login"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        errors = []

        if database.is_user_exists(login):
            errors.append("такой пользователь уже существует")

        if len(pass1) < 4:
            errors.append("пароль должен быть минимум 4 символа")

        if pass1 != pass2:
            errors.append("пароли не совпадают")
        if len(errors) == 0:
            database.add_user(login,pass1)
            return render_template("login.html")
        else:
            return render_template("register.html", errors=errors)
if __name__ == "__main__":
    app.run(debug=True)