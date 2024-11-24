from flask import Flask,request

add_app=Flask(__name__)

@add_app.route("/add",methods=["GET"])
def add_function():
    num1 = request.args.get("num1", type=float)  # Default type is float for flexibility
    num2 = request.args.get("num1", type=float)  # Default type is float for flexibility

    if num1 is None or num2 is None:
        return "Please provide both 'num1' and 'num2' as query parameters.", 400
    
    return f"The sum of two {num1} and {num2} is {num1+num2}"

@add_app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@add_app.route('/hello1/<name>')
def hello_name1(name):
   return 'Hello %s!' % name




if __name__=="__main__":
    add_app.run(debug=True)


    