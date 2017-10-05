from flask import Flask, request, redirect, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home")
def display_home():
    return render_template("home.html", title="Sign Me Up")

def valid_username(name):
    
    if len(name) == 0 or < 3:
        return error
    elif name 



@app.route("/home", methods=["POST"])
def home():
    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ""
    pass_error = ""
    email_error = ""

    if username

    return render_template("home.html", title="Sign me up")


@app.route("/welcome")
def welcome():

    user_name = request.form['username']
    return render_template("welcome.html", title="HEY THERE!!")



app.run()