

from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     title = "NYU PROJECT EMAIL NOTIFICATIONS"
#     return render_template("index.html", title= title)

@app.route('/')
def index():
    return ("hello")


# @app.route('/about')
# def about():
#     title = "About me"
#     names= ["john","shngyu","wes","sally"]
#     return render_template("about.html", title= title)

# tutorial
# https://www.youtube.com/watch?v=2e4STDACVA8&list=PLCC34OHNcOtqJBOLjXTd5xC0e-VD3siPn&index=2&ab_channel=Codemy.com