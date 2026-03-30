import requests
from flask import Flask, render_template,url_for
import requests as rt
app = Flask(__name__)
from datetime import datetime

@app.route('/')
def hello_world():
    year = datetime.now().year
    return render_template('index.html', year=year)

@app.route('/guess/<string:name>')
def guess(name):
    age = rt.get(f"http://api.agify.io/?name={name}").json()
    gender = rt.get(f"https://api.genderize.io?name={name}").json()
    return render_template('report.html', age=age["age"], gender=gender["gender"], name=name)

@app.route("/blog")
def go_to_blog():
    blog_posts = rt.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template('blog.html',posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)