from flask import Flask, request, redirect, render_template
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home")
def display_home():
    return render_template("home.html", title="Sign Me Up")

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def containsAll(str, set):
    #"""Check whether 'str' contains ALL of the chars in 'set'"""
    return 0 not in [c in str for c in set]

@app.route("/home", methods=["POST"])
def home():
    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ""
    pass_error = ""
    email_error = ""
    verify_error = ""

    if len(username) < 3 or len(username) > 20:
        user_error = "Username does not fit the required length"
        username = ""
    elif not is_ascii(username):
        user_error = "Please use correct characters"
        username = ""

    if len(password) < 3 or len(password) > 20:
        pass_error = "Password does not fit the required length"
        password = ""
    elif not is_ascii(password):
        pass_error = "Please use correct characters"
        password = ""

    if password != verify: 
        pass_error = "Please make sure your passwords match"
        password = ""
        verify = ""
    
    if len(email) != 0:
        email_error = "Make sure this is a correct email address"
        email = ""
    
    if len(email) == 0:
        if len(verify) != 0:
            if len(password) != 0:
                if len(username) != 0:
                    username = request.form["username"]
                    return render_template("welcome.html", username=username)
                else:
                    return render_template("home.html", user_error=user_error, pass_error=pass_error, email_error=email_error,
                        username=username, email=email, password=password, verify=verify)
            else:
                return render_template("home.html", user_error=user_error, pass_error=pass_error, email_error=email_error,
                    username=username, email=email, password=password, verify=verify)
        else:
            return render_template("home.html", user_error=user_error, pass_error=pass_error, email_error=email_error,
                username=username, email=email, password=password, verify=verify)
    else:
        if len(email) != 0 and containsAll("@."):
            
            if len(verify) != 0:
                if len(password) != 0:
                    if len(username) != 0:
                        username = request.form["username"]
                        return render_template("welcome.html", username=username)
                    else:
                        return render_template("home.html", user_error=user_error, pass_error=pass_error, email_error=email_error,
                            username=username, email=email, password=password, verify=verify)
                else:
                    return render_template("home.html", user_error=user_error, pass_error=pass_error, email_error=email_error,
                        username=username, email=email, password=password, verify=verify)
            else:
                return render_template("home.html", user_error=user_error, pass_error=pass_error, email_error=email_error,
                    username=username, email=email, password=password, verify=verify)



#@app.route("/welcome", methods=['POST'])
#def welcome():
 #   username = request.form["username"]
  #  return render_template("welcome.html", username = username)



app.run()