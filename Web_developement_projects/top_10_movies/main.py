import time

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, os

TMDB_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NTg2NjZiNWJkOWU4NjMyZGU0YzA5ZGNjNTc3YjBjNiIsIm5iZiI6MTc3Mjc3ODg0Ni41MTgwMDAxLCJzdWIiOiI2OWFhNzU1ZTkyNjg3YWEyYzE2YWNhZDciLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.lSA9cLZQMrgIR_7Dt0cvCzMNMBLKnm0eF_uy3wQEvms"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'top-movies.db')

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String,unique=True,nullable=False)
    year: Mapped[int] = mapped_column(Integer,nullable=False)
    description: Mapped[str] = mapped_column(String,nullable=False)
    rating: Mapped[float] = mapped_column(Float,nullable=False)
    ranking: Mapped[int] = mapped_column(Integer,nullable=False)
    review: Mapped[str] = mapped_column(String,nullable=False)
    img_url: Mapped[str] = mapped_column(String,nullable=False)

with app.app_context():
    db.create_all()

def search_movie_by_name(movie_name):
    print(movie_name)
    parameters = {
        "query": movie_name
    }
    headers = {"accept": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NTg2NjZiNWJkOWU4NjMyZGU0YzA5ZGNjNTc3YjBjNiIsIm5iZiI6MTc3Mjc3ODg0Ni41MTgwMDAxLCJzdWIiOiI2OWFhNzU1ZTkyNjg3YWEyYzE2YWNhZDciLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.lSA9cLZQMrgIR_7Dt0cvCzMNMBLKnm0eF_uy3wQEvms"}
    response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters, headers=headers, verify=False)
    data = response.json()
    # This returns a list of dictionaries (all matching movies)
    return data["results"]

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = i + 1  # 1st movie = 1, 2nd = 2...

    db.session.commit()
    return render_template("index.html",movies=all_movies)

@app.route("/edit/<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    edit_movie = Movie.query.get(movie_id)
    edit_form = RateMovieForm()
    if request.method == "POST":
        edit_movie.rating = float(edit_form.rating.data)
        edit_movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))


    return render_template("edit.html", movie = edit_movie, form = edit_form)

@app.route("/delete/<movie_id>")
def delete(movie_id):
    delete_movie = Movie.query.get(movie_id)
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        movie_title = request.form["title"]
        result = search_movie_by_name(movie_title)
        return render_template("select.html", options=result)
    return render_template("add.html")


@app.route("/find")  # No need for POST here, we are only 'getting' data
def find():
    movie_api_id = request.args.get("id")
    print(movie_api_id)
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        headers = {"accept": "application/json", "Authorization": f"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NTg2NjZiNWJkOWU4NjMyZGU0YzA5ZGNjNTc3YjBjNiIsIm5iZiI6MTc3Mjc3ODg0Ni41MTgwMDAxLCJzdWIiOiI2OWFhNzU1ZTkyNjg3YWEyYzE2YWNhZDciLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.lSA9cLZQMrgIR_7Dt0cvCzMNMBLKnm0eF_uy3wQEvms"}
        response = requests.get(movie_api_url, headers=headers, verify=False)
        print(response.status_code)
        data = response.json()
        print(data)
        # Check if the movie already exists to prevent crashes
        new_movie = Movie(
            title=data["title"],
            # Using .split("-")[0] is great, but ensure release_date exists
            year=data.get("release_date", "0000").split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"],
            rating=0,
            ranking=0,
            review="None"
        )

        db.session.add(new_movie)
        db.session.commit()

        # Redirect using the NEW database ID, not the TMDB ID
        return redirect(url_for('edit', movie_id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
