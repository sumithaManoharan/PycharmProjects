from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)

db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(db.String(250), nullable=False)
    rating: Mapped[float] = mapped_column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    query = db.select(Book).order_by(Book.title)
    result = db.session.execute(query)
    all_books = result.scalars().all()
    print(all_books)


    return render_template('index.html', books=all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
            new_book = Book(title=request.form.get("book_name"), author=request.form.get("author"), rating=request.form.get("rating"))
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/delete/<int:id>")
def delete(id):
    with app.app_context():
        book_to_delete = Book.query.get(id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))

@app.route("/edit/<int:eid>", methods=['GET','POST'])
def edit(eid):
    print(eid)
    if request.method == 'POST':
        with app.app_context():
            book_to_update = Book.query.get(eid)
            book_to_update.rating = request.form.get('rating')
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html',book=Book.query.get(eid))

# @app.route("/add/<int:id>", methods=['GET','POST'])


if __name__ == "__main__":
    app.run(debug=True)


