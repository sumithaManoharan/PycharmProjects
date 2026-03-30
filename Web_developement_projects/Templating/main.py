from flask import Flask, render_template, url_for
import requests as rt
from post import Post
blog_posts = rt.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",posts=blog_posts)

@app.route('/blog/<int:post_id>')
def get_blog(post_id):
    body,title,subtitle = Post(blog_posts, post_id).render()
    return render_template("post.html",body=body,title=title,subtitle=subtitle)


if __name__ == "__main__":
    app.run(debug=True)
