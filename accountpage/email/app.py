

from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     title = "NYU PROJECT EMAIL NOTIFICATIONS"
#     return render_template("index.html", title= title)

@app.route('/')
def index():
    return ("hello")


@app.route('/subscribe')
def subscribe():
    title = "subscribe to my email new sletter"
    return render_template(subscribe.html,title=title)

@app.route('/form',method=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    if not first_name or not last_name or not email:
        error_statement = "all form fields required..."
    subscribe.append(f"{first_name}{last_name}"| {email title="thank you"})
    title = "thank you!"
    return render_template("form.html",title=title)
def subscribe():

def index():
    return ("hello")

# @app.route('/about')
# def about():
#     title = "About me"
#     names= ["john","shngyu","wes","sally"]
#     return render_template("about.html", title= title)

# tutorial
# https://www.youtube.com/watch?v=2e4STDACVA8&list=PLCC34OHNcOtqJBOLjXTd5xC0e-VD3siPn&index=2&ab_channel=Codemy.com