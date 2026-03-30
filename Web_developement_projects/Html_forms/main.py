from flask import Flask,render_template,request as rt


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=['Post'])
def login():
    username = rt.form.get("username")
    password = rt.form.get("password")
    return render_template("page_1.html",username=username,password=password)

if __name__ == "__main__":
    app.run(debug=True)