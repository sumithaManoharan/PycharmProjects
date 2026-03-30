from flask import Flask, render_template, url_for, request, redirect
import requests as rt
from post import Post

blogs = rt.get("https://api.npoint.io/733ab662b0ff06934e57").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",blogs=blogs)

@app.route('/blogs/<int:pid>')
def get_blogs(pid):
    body,title,subtitle ,image= Post().render(blogs,pid)
    return render_template("blogs.html",body=body,title=title,subtitle=subtitle,image=image)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/post')
def get_post():
    return render_template("post.html")

@app.route('/contact')
def get_contact():
    return render_template("contact.html")

@app.route('/get_info', methods=['POST'])
def get_info():
    name=request.form.get('name')
    email=request.form.get('email')
    phone=request.form.get('phone')
    message=request.form.get('message')
    Post().send_email(name,email,phone,message)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True,host="localhost",port=5000)