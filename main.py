import uuid

from flask import Flask, render_template, redirect, url_for, request, session
from PIL import Image, ImageDraw, ImageFont
import database
import os

app = Flask(__name__)
app.secret_key = "a3487wgeyufrt2673g4yug"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

imges = database.get_pictures(5)
print(imges)
print(imges)
print(imges)
print(imges)
print(imges)

@app.route("/")
def index():
    
    if "login" not in session:
        return redirect(url_for("login"))
    
    return render_template("index.html", login=session["login"])

@app.route("/creater", methods=["POST","GET"])
def creater():
    if request.method == "GET":
        ...
    elif request.method == "POST":
        print(request.form)
        img_url = request.form.get("image")
        return render_template("creater.html", image_url=img_url)

        

    return render_template("creater.html", image_url=img_url)

@app.route("/creater_img", methods=["POST"])
def creater_img():
    print("robit ili net")
    img_url = request.form.get("image")
    img_url = img_url.lstrip("/")

    image_path = os.path.join(BASE_DIR, img_url)
    
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    text = request.form.get("img_text")

    x = int(request.form.get("x"))
    y = int(request.form.get("y"))
    
    font_size = int(request.form.get("font_size"))

    font = ImageFont.truetype("arial.ttf", size=font_size)
    
    text_color = (0, 0, 0)

    draw.text((x, y), text, fill=text_color, font=font)
    
    output_name = f"{uuid.uuid4()}.jpg"
    
    output_path = os.path.join("static/img", output_name)
    
    image.save(output_path)
    
    database.add_picture("static/img/"+(output_name),session["user_id"])

    return redirect(f"/static/img/{output_name}")

@app.route("/gareley")
def gareley():
    images = []
    return render_template("gareley.html",imgs=images)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        login = request.form['login']
        password = request.form["password"]

        auth_user = database.auth_user(login, password)
        if auth_user == None:
            return render_template(
                "login.html",
                errors=["Неверный логин или пароль"]
            )
        else:
            print('успешный вход')
            session["user_id"] = auth_user["user_id"]
            session["login"] = auth_user["user_login"]
            return redirect(url_for('index'))

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

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))    
    
if __name__ == "__main__":
    app.run(debug=True)