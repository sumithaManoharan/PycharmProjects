import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def to_bool(self,value):
        if value == "True" or value == "true":
            return True
        elif value == "False":
            return False
        else:
            return None




with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    cafe =random.choice(cafes)
    return jsonify(cafe.to_dict())

@app.route("/all")
def get_all():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return {"cafes":[cafe.to_dict() for cafe in cafes]}

@app.route("/search")
def search():
    location = request.args.get('loc')
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# HTTP POST - Create Record
@app.route("/add_cafe",methods=["POST"])
def add_cafe():
    def to_bool(value):
        if value == "True" or value == "true":
            return True
        elif value == "False"or value == "false":
            return False
        else:
            return None
    new_cafe = Cafe(
        name= request.args.get('name'),
        map_url = request.args.get('map_url'),
        img_url= request.args.get('img_url'),
        location= request.args.get('loc'),
        seats = request.args.get('seats'),
        has_toilet = to_bool(request.args.get('has_toilet')),
        has_wifi = to_bool(request.args.get('has_wifi')),
        has_sockets =  to_bool(request.args.get('has_sockets')),
        can_take_calls = to_bool(request.args.get('can_take_calls')),
        coffee_price = request.args.get('coffee_price'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added new cafe"}), 201



# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods = ["PATCH"])
def update_price(cafe_id):
    try:
        cafe = db.session.get(Cafe, cafe_id)
        print(cafe)
        if cafe:
            attr = request.args.get('new_price')
            cafe.coffee_price = attr
            db.session.commit()
            return jsonify(response={"Success": "price updated Successfully"}), 201
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that id."}), 404
    except Exception as e:
        return f"error: {e}"

# HTTP DELETE - Delete Record

@app.route("/report-closed/<cafe_id>")
def report_closed(cafe_id):
    try:
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Successfully closed cafe"}), 201
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that id."}), 404
    except Exception as e:
        return f"error: {e}"


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
