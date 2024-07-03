#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>", methods=["GET"])
def print_string(parameter):
    print(parameter)

    return parameter
  

@app.route("/count/<int:parameter>", methods=["GET"])
def count(parameter):
    numbers=list(range(parameter))
    
    numbers_str="\n".join(str(num) for num in numbers)
    return f"<pre>{numbers_str}</pre>"


@app.route("/math/<int:num1>/<string:operation>/<int:num2>",methods=["GET"])
def math(num1,operation,num2):
    if operation=="+":
        result= num1 + num2
    elif operation=="-":
        result= num1 - num2
    elif operation=="*":
        result =num1 * num2
    elif operation=="div":
        result= num1 / num2
    elif operation=="%":
        result =num1 % num2
    else:
        return"Invalid operation",400
    
    return str(result)


    

if __name__ == '__main__':
    app.run(port=5000, debug=True)
