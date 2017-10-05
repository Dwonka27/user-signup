from flask import Flask, request, redirect, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/home", methods=["POST", "GET"])
def home():
    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ""
    
    pass_error = ""
    email_error = ""

    

    return render_template("home.html", title="Sign Me Up")


@app.route("/welcome")
def welcome():

    return render_template("welcome.html", title="HEY THERE!!")