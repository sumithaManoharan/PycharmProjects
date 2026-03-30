from flask import Flask

def make_bold(function):
    def wrapper():
        text = function()
        return "<b><u><em>" + text + "</em><u/></b>"
    return wrapper

app = Flask(__name__)

@app.route("/hi")
@make_bold
def hello_world():
    return "Hello World!"

# @app.route("/<name>/end")
# def hello(name):
#     return f"Hello World {name}!"

if __name__ == "__main__":
    app.run(debug=True)


# decorator function ads functionality to the existing function
# import time
# def decorator_function(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function
#
# @decorator_function
# def hello():
#     print("Hello World")
#
# def bye():
#     print("Bye World")
#
# def greet():
#     print("Hello how are you?")
#
# bye()

# # TODO: Create the logging_decorator() function 👇
#
# def logging_decorator(function):
#     def wrapper(*args):
#         print(f"You called {function.__name__}{(args)}")
#         result = function(*args)
#         print(f"It returned: {result}")
#         return result
# 
#     return wrapper
#
#
# # TODO: Use the decorator 👇
# @logging_decorator
# def a_function(*args):
#     return sum(args)
#
#
# a_function(1, 2, 3)