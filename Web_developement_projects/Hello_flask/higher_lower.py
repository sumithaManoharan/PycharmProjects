from flask import Flask
import random
number = random.randint(0, 9)
app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>\n<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWpmODE1YTU1enEybDUyMWphcWx5M20zMXVrcHFtYnExeTkxdXoydSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="numbers"/>'

@app.route("/<int:guess>")
def guess_number(guess):
    if guess == number:
        return '<h1 style="color:purple">You found me!</h1>\n<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="puppy"/>'
    if guess > number:
        return '<h1 style="color:red">Too high, try again!</h1>\n<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="puppy"/>'
    if guess < number:
        return '<h1 style="color:blue">Too low, try again!</h1>\n<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="puppy"/>'


if __name__ == "__main__":
    app.run(debug=True)