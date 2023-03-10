

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "NYU PROJECT EMAIL NOTIFICATIONS"
    return render_template("index.html", title= title)
    
@app.route('/about')
def about():
    title = "About me"
    names= ["john","shngyu","wes","sally"]
    return render_template("about.html", title= title)