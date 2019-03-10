from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
from dataSetGenerator import rec
from detector import detect

@app.route('/')
def test():
	return render_template("index.html")

@app.route('/success/<name>')
def success(name):
   rec(name)
   return render_template("success.html",id = name)

@app.route('/detect',methods = ['POST', 'GET'])
def det():
   if request.method == 'POST':
      detect()
      return render_template("done.html")
      

@app.route('/name',methods = ['POST', 'GET'])
def recv():
   if request.method == 'POST':
      name = request.form['name']
      return redirect(url_for('success',name = name))


# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name

# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#    return 'Blog Number %d' % postID

# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#    return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run(debug = True)

# @app.route('/')
# def hello_world():
# 	return 'Hello World'

# if __name__ == '__main__':
# 	app.debug = True
# 	app.run()
# 	app.run(debug = True)