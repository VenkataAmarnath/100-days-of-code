from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route("/hello/<name>")
def hellp_name(name):
    return "Hello %s" % name

@app.route("/blog/<int:id>")
def blog_id(id):
    return "Blog id is %d" % id

@app.route('/rev/<float:revNo>') 
def revision(revNo): 
    return 'Revision Number %f' % revNo 

@app.route("/admin")
def hello_admin():
    return "Hello admin"

@app.route("/guest/<name1>")
def hello_guest(name1):
    return "Hello %s" %name1


@app.route("/redirect/<name>")
def hellooo(name):
    if name=="admin":
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',name1=name))


@app.route("/hello1")
def hello1():
    return render_template('index.html')


















if __name__ == '__main__':
    app.run(debug=True)